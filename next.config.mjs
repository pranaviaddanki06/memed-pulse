/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  basePath: '/memed-pulse',
  images: { unoptimized: true },
  experimental: { typedRoutes: false }
};
export default nextConfig;
