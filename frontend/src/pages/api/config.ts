import type { NextApiRequest, NextApiResponse } from 'next';

interface ConfigResponse {
    API_URL?: string;
}

export default function handler(req: NextApiRequest, res: NextApiResponse<ConfigResponse>) {
    res.status(200).json({
        API_URL: process.env.NEXT_PUBLIC_API_URL
    });
}
