// src/context/ConfigContext.tsx
import { createContext, useContext, ReactNode, useState } from 'react';

interface Config {
    API_URL?: string;  // Extend this interface based on the actual data you expect
}

const ConfigContext = createContext<Config>({});

export const useConfig = () => useContext(ConfigContext);

export const ConfigProvider: React.FC<{ children: ReactNode, value: Config }> = ({ children, value }) => {
    return (
        <ConfigContext.Provider value={value}>
            {children}
        </ConfigContext.Provider>
    );
};
