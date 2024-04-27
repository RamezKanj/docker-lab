import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { useEffect, useState } from 'react';
import { ConfigProvider } from '../context/ConfigContext';

export default function App({ Component, pageProps }: AppProps) {
    const [config, setConfig] = useState({});

    useEffect(() => {
        fetch('/api/config')
            .then(res => res.json())
            .then(data => {
                setConfig(data);
            })
            .catch(error => console.error('Failed to load configuration:', error));
    }, []);

    return (
        <ConfigProvider value={config}>
            <Component {...pageProps} />
        </ConfigProvider>
    );
}
