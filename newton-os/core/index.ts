/**
 * ═══════════════════════════════════════════════════════════════════════════
 * NEWTON OS - CORE MODULE
 * ═══════════════════════════════════════════════════════════════════════════
 * 
 * The core of Newton OS.
 * 
 * Layer 0: NBezierObject - The universal shape (continuous, no discontinuities)
 * Layer 1: NObject - The universal object (reactive, verified)
 * Layer 2: NObjectGraph - The data soup (query by constraint, not path)
 * Layer 3: NewtonProtocol - The verification bridge (to Newton Agent)
 * 
 * ═══════════════════════════════════════════════════════════════════════════
 */

// Layer 0: The Bezier Primitive
export { 
  Point,
  BezierSegment,
  SuperellipseParams,
  NBezierObject,
  NShapes,
} from './bezier';

// Layer 1: The Universal Object
export {
  NObject,
  NObjectId,
  NValue,
  NProperty,
  NRelationship,
  RelationshipKind,
  NObjectTypes,
  NObjectFactory,
} from './nobject';

// Layer 2: The Object Graph
export {
  NObjectGraph,
  NConstraint,
  NQueryResult,
  NGraphMutation,
  TheGraph,
} from './graph';

// Layer 3: The Newton Protocol
export {
  NewtonProtocol,
  NewtonRequest,
  NewtonResponse,
  LedgerEntry,
  VerificationResult,
  VerifiedGraph,
  Newton,
} from './protocol';
