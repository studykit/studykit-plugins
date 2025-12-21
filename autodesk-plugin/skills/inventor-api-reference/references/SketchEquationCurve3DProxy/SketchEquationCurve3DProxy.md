# SketchEquationCurve3DProxy Object

Derived from: [SketchEquationCurve3D](../SketchEquationCurve3D/SketchEquationCurve3D.md) Object

## Description

Represents a part SketchEquationCurve3D in an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [GetEquation](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_GetEquation.md) | Method that returns all of the information that defines the equatino for this curve. To edit use the SetEquation method. |
| [GetReferenceKey](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEquation](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_SetEquation.md) | Method that returns all of the information that defines the equatino for this curve. To edit use the SetEquation method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CurvatureDisplay](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the curve. |
| [EndSketchPoint](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_EndSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the end of the curve. |
| [Geometry](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Geometry.md) | Read-only property that gets a BSplineCurve2d geometry object. The object returned represents a 'snapshot' view of the current state of the spline. |
| [HasReferenceComponent](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Length.md) | Gets the length of the entity in centimeters. |
| [NativeObject](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_StartSketchPoint.md) | Read-only property that gets the sketch point that defines the position of the start of the sketch spline. |
| [Type](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2014
