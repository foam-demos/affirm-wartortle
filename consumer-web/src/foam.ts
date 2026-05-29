import * as foam from '@foam-ai/node-opentelemetry';
import { FOAM_API_KEY, IS_PRODUCTION } from './config/keys';
import { ExpressInstrumentation } from '@opentelemetry/instrumentation-express';
import type { InstrumentationBase } from '@opentelemetry/instrumentation';

foam.init({
  serviceName: 'consumer-web',
  isProduction: IS_PRODUCTION,
  apiKey: `Bearer ${FOAM_API_KEY}`,
  additionalInstrumentations: [
    new ExpressInstrumentation({}) as unknown as InstrumentationBase
  ],
  captureConsoleErrors: true,
  captureUnhandledRejections: true
});