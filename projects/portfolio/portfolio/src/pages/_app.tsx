// Tutorial to implement multiple layouts: https://www.codeconcisely.com/posts/nextjs-multiple-layouts/
import type { AppProps } from "next/app"


export default function App({ Component, pageProps }: AppProps) {
  return (
          <Component {...pageProps} />
  );
}