# IntersectionCurve Object

## Description

The IntersectionCurve object represents the results of creating an intersection curve calculation. It consists of one or more sketch entities that represent the intersection of the original input entities.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../IntersectionCurve/IntersectionCurve_BreakLink.md) | Method that breaks the link between the intersection curve and the model. This breaks the associativity to the model, allowing you to edit the individual sketch entities. |
| [Delete](../IntersectionCurve/IntersectionCurve_Delete.md) | Method that deletes the intersection curve. This will delete all of the related sketch entities. |
| [Edit](../IntersectionCurve/IntersectionCurve_Edit.md) | Method that edits all of the inputs used to compute the intersection curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit. |
| [GetReferenceKey](../IntersectionCurve/IntersectionCurve_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../IntersectionCurve/IntersectionCurve_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../IntersectionCurve/IntersectionCurve_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [EntityOne](../IntersectionCurve/IntersectionCurve_EntityOne.md) | Read-write property that defines the first entity involved in the intersection. |
| [EntityTwo](../IntersectionCurve/IntersectionCurve_EntityTwo.md) | Read-write property that defines the second entity(s) involved in the intersection. |
| [Name](../IntersectionCurve/IntersectionCurve_Name.md) | Property that gets and sets name of the intersection curve. |
| [Parent](../IntersectionCurve/IntersectionCurve_Parent.md) | Read-only property that returns the parent 3D sketch of the intersection curve. |
| [SketchEntities](../IntersectionCurve/IntersectionCurve_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to the intersection curve. The sketch entities returned by this property cannot be edited or deleted because they are associated with the intersection curve in the model. The BreakLink method can be used to break this association so they are individually editable. |
| [Type](../IntersectionCurve/IntersectionCurve_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[IntersectionCurve.Edit](../IntersectionCurve/IntersectionCurve_Edit.md), [IntersectionCurveProxy.Edit](../IntersectionCurveProxy/IntersectionCurveProxy_Edit.md), [IntersectionCurveProxy.NativeObject](../IntersectionCurveProxy/IntersectionCurveProxy_NativeObject.md), [IntersectionCurves.Add](../IntersectionCurves/IntersectionCurves_Add.md), [IntersectionCurves.Item](../IntersectionCurves/IntersectionCurves_Item.md)

## Derived Classes

[IntersectionCurveProxy](../IntersectionCurveProxy/IntersectionCurveProxy.md)

## Version

Introduced in version 2014
