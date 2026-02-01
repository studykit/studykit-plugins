# SketchPoint3DProxy Object

Derived from: [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConnectTo](../SketchPoint3DProxy/SketchPoint3DProxy_ConnectTo.md) | Method that connects this sketch point to the input point. Valid inputs are SketchPoint3D, SketchPoint, Vertex or WorkPoint. This method is the UI equivalent of 'Add Coincident Constraint'. The point being constrained is the sketch point on which this method is called and the input point is the constraining point. This method will fail if a coincident constraint exists between this sketch point and a vertex; i.e. this sketch point must be underconstrained. |
| [Delete](../SketchPoint3DProxy/SketchPoint3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchPoint3DProxy/SketchPoint3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MoveBy](../SketchPoint3DProxy/SketchPoint3DProxy_MoveBy.md) | Method that moves the sketch point a delta distance from its current location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified. |
| [MoveTo](../SketchPoint3DProxy/SketchPoint3DProxy_MoveTo.md) | Method that moves the sketch point to an explicit x-y-z location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchPoint3DProxy/SketchPoint3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttachedEntities](../SketchPoint3DProxy/SketchPoint3DProxy_AttachedEntities.md) | Property that returns the collection of objects that are connected to this point. |
| [AttributeSets](../SketchPoint3DProxy/SketchPoint3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchPoint3DProxy/SketchPoint3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchPoint3DProxy/SketchPoint3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchPoint3DProxy/SketchPoint3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchPoint3DProxy/SketchPoint3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Geometry](../SketchPoint3DProxy/SketchPoint3DProxy_Geometry.md) | Gets and sets a Point geometry object. The object returned represents a 'snapshot' view of the current state of the sketch point. |
| [HasReferenceComponent](../SketchPoint3DProxy/SketchPoint3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HoleCenter](../SketchPoint3DProxy/SketchPoint3DProxy_HoleCenter.md) | Defines if the sketch point is being displayed as a hole center. |
| [NativeObject](../SketchPoint3DProxy/SketchPoint3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchPoint3DProxy/SketchPoint3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchPoint3DProxy/SketchPoint3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchPoint3DProxy/SketchPoint3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchPoint3DProxy/SketchPoint3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchPoint3DProxy/SketchPoint3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchPoint3DProxy/SketchPoint3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [Type](../SketchPoint3DProxy/SketchPoint3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
