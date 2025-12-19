import { useEffect, useRef, useState } from "react";

type MicState = "idle" | "starting" | "active" | "stopped" | "error";

export function useMicrophone() {
  const [state, setState] = useState<MicState>("idle");
  const [error, setError] = useState<string | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const audioCtxRef = useRef<AudioContext | null>(null);
  const sourceRef = useRef<MediaStreamAudioSourceNode | null>(null);

  async function start() {
    try {
      setState("starting");
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      streamRef.current = stream;

      const audioCtx = new AudioContext();
      audioCtxRef.current = audioCtx;
      const source = audioCtx.createMediaStreamSource(stream);
      sourceRef.current = source;

      setState("active");
      setError(null);
      return { stream, audioCtx, source };
    } catch (e: any) {
      setError(e?.message ?? "Microphone access failed");
      setState("error");
      return null;
    }
  }

  function stop() {
    try {
      streamRef.current?.getTracks().forEach(t => t.stop());
      audioCtxRef.current?.close();
      streamRef.current = null;
      sourceRef.current = null;
      audioCtxRef.current = null;
      setState("stopped");
    } catch (e: any) {
      setError(e?.message ?? "Stop failed");
      setState("error");
    }
  }

  useEffect(() => {
    return () => stop();
  }, []);

  return { state, error, start, stop, streamRef, audioCtxRef, sourceRef };
}
