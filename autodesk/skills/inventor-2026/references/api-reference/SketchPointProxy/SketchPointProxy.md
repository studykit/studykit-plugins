# SketchPointProxy Object

Derived from: [SketchPoint](../SketchPoint/SketchPoint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchPointProxy/SketchPointProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetReferenceKey](../SketchPointProxy/SketchPointProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Merge](../SketchPointProxy/SketchPointProxy_Merge.md) | Method that merges this sketch point with the input sketch point. Any objects dependent on this sketch point will change their dependency to the new sketch point. |
| [MoveBy](../SketchPointProxy/SketchPointProxy_MoveBy.md) | Method that moves the sketch point a delta distance from its current location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified. |
| [MoveTo](../SketchPointProxy/SketchPointProxy_MoveTo.md) | Method that moves the sketch point to an explicit X-Y location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchPointProxy/SketchPointProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttachedEntities](../SketchPointProxy/SketchPointProxy_AttachedEntities.md) | Property that returns the collection of objects that are connected to this point. |
| [AttributeSets](../SketchPointProxy/SketchPointProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConnectionPoint](../SketchPointProxy/SketchPointProxy_ConnectionPoint.md) | Gets and sets whether the point behaves as a connection point or not. |
| [Constraints](../SketchPointProxy/SketchPointProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchPointProxy/SketchPointProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchPointProxy/SketchPointProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchPointProxy/SketchPointProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchPointProxy/SketchPointProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [DisabledActionTypes](../SketchPointProxy/SketchPointProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [Geometry](../SketchPointProxy/SketchPointProxy_Geometry.md) | Property that returns a Point2d geometry object. The object returned represents a snapshot view of the current state of the sketch point. |
| [Geometry3d](../SketchPointProxy/SketchPointProxy_Geometry3d.md) | Read-only property that returns point geometry that represents this point in model space. |
| [HasReferenceComponent](../SketchPointProxy/SketchPointProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HoleCenter](../SketchPointProxy/SketchPointProxy_HoleCenter.md) | Gets and sets whether the point behaves as a hole center or not. |
| [InsertionPoint](../SketchPointProxy/SketchPointProxy_InsertionPoint.md) | Gets and sets whether the point behaves as an insertion point or not. |
| [Layer](../SketchPointProxy/SketchPointProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [NativeObject](../SketchPointProxy/SketchPointProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchPointProxy/SketchPointProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchPointProxy/SketchPointProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchPointProxy/SketchPointProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchPointProxy/SketchPointProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchPointProxy/SketchPointProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchPointProxy/SketchPointProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchPointProxy/SketchPointProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchPointProxy/SketchPointProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [Type](../SketchPointProxy/SketchPointProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
