import {analyze,embed,corpus} from '../lib/engine';
const a=analyze({caption:'The cricket final is iconic!',category:'cricket',audience:'Gen Z'});
if(a.score<0||a.score>100)throw Error('invalid score');if(a.similar.length!==6)throw Error('retrieval failed');if(Math.abs(Math.hypot(...embed('hello'))-1)>1e-9)throw Error('embedding not normalized');if(corpus.length!==300)throw Error('seed missing');
