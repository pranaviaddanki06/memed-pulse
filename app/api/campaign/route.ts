import { analyze } from '@/lib/engine';

export async function POST(req: Request) {
  try {
    const x = await req.json();
    const captions = [
      `A relatable ${x.tone || 'bold'} moment for ${x.brand || 'your brand'}`,
      `The conversation ${x.brand || 'this campaign'} starts today`,
      'A small moment with a big cultural signal',
    ];

    return Response.json({
      concepts: captions.map((caption) => ({
        ...analyze({
          caption,
          category: 'relatable',
          audience: x.audience || 'Gen Z',
          objective: x.objective,
        }),
        caption,
      })),
    });
  } catch {
    return Response.json({ error: 'Invalid campaign request' }, { status: 400 });
  }
}
