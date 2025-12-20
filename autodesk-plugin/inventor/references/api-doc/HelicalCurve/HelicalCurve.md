# HelicalCurve Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

HelicalCurve object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HelicalCurve/HelicalCurve_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../HelicalCurve/HelicalCurve_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HelicalCurve/HelicalCurve_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HelicalCurve/HelicalCurve_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../HelicalCurve/HelicalCurve_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../HelicalCurve/HelicalCurve_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../HelicalCurve/HelicalCurve_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [Definition](../HelicalCurve/HelicalCurve_Definition.md) | Gets and sets the shape definition of the helical curve. |
| [HasReferenceComponent](../HelicalCurve/HelicalCurve_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Name](../HelicalCurve/HelicalCurve_Name.md) | Gets and sets the name of the helical curve. |
| [OwnedBy](../HelicalCurve/HelicalCurve_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../HelicalCurve/HelicalCurve_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../HelicalCurve/HelicalCurve_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../HelicalCurve/HelicalCurve_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../HelicalCurve/HelicalCurve_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../HelicalCurve/HelicalCurve_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [SketchEntities](../HelicalCurve/HelicalCurve_SketchEntities.md) | Returns a collection of sketch entities that belong to the helical curve. |
| [Type](../HelicalCurve/HelicalCurve_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HelicalCurveConstantShapeDefinition.Parent](../HelicalCurveConstantShapeDefinition/HelicalCurveConstantShapeDefinition_Parent.md), [HelicalCurveDefinition.Parent](../HelicalCurveDefinition/HelicalCurveDefinition_Parent.md), [HelicalCurveProxy.NativeObject](../HelicalCurveProxy/HelicalCurveProxy_NativeObject.md), [HelicalCurves.Add](../HelicalCurves/HelicalCurves_Add.md), [HelicalCurves.Item](../HelicalCurves/HelicalCurves_Item.md), [HelicalCurveVariableShapeDefinition.Parent](../HelicalCurveVariableShapeDefinition/HelicalCurveVariableShapeDefinition_Parent.md)

## Derived Classes

[HelicalCurveProxy](../HelicalCurveProxy/HelicalCurveProxy.md)

## Version

Introduced in version 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |