/** @type {import('next').NextConfig} */
const isGithubPages = process.env.GITHUB_ACTIONS === 'true';
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  basePath: isGithubPages ? '/memed-pulse' : '',
  assetPrefix: isGithubPages ? '/memed-pulse/' : '',
  images: { unoptimized: true },
  experimental: { typedRoutes: false }
};
export default nextConfig;
