# SilhouetteCurve Object

## Description

SilhouetteCurve Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../SilhouetteCurve/SilhouetteCurve_BreakLink.md) | Method that breaks the link between the silhouette curve and the model. |
| [Delete](../SilhouetteCurve/SilhouetteCurve_Delete.md) | Method that deletes the silhouette curve. This will delete all of the related sketch entities. |
| [Edit](../SilhouetteCurve/SilhouetteCurve_Edit.md) | Method that edits all of the inputs used to compute the silhouette curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit. |
| [GetReferenceKey](../SilhouetteCurve/SilhouetteCurve_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SilhouetteCurve/SilhouetteCurve_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SilhouetteCurve/SilhouetteCurve_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Body](../SilhouetteCurve/SilhouetteCurve_Body.md) | Read-write property that defines the surfaces the silhouette is calculated for. |
| [DirectionEntity](../SilhouetteCurve/SilhouetteCurve_DirectionEntity.md) | Read-write property gets and set the direction used to calculate the silhouette curve. |
| [ExcludedFaces](../SilhouetteCurve/SilhouetteCurve_ExcludedFaces.md) | Read-write property that gets and sets the faces that are excluded in the silhouette curve projection. |
| [ExcludeInternalFaces](../SilhouetteCurve/SilhouetteCurve_ExcludeInternalFaces.md) | Read-write property that specifies whether to exclude the internal faces from the silhouette curve projection. |
| [ExcludeStraightFaces](../SilhouetteCurve/SilhouetteCurve_ExcludeStraightFaces.md) | Read-write property that specifies whether to exclude the faces that are perpendicular to the project direction from the silhouette curve projection. |
| [Name](../SilhouetteCurve/SilhouetteCurve_Name.md) | Property that gets and sets name of the silhouette curve. |
| [Parent](../SilhouetteCurve/SilhouetteCurve_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SketchEntities](../SilhouetteCurve/SilhouetteCurve_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to silhouette curve. |
| [Type](../SilhouetteCurve/SilhouetteCurve_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SilhouetteCurve.Edit](../SilhouetteCurve/SilhouetteCurve_Edit.md), [SilhouetteCurveProxy.Edit](../SilhouetteCurveProxy/SilhouetteCurveProxy_Edit.md), [SilhouetteCurveProxy.NativeObject](../SilhouetteCurveProxy/SilhouetteCurveProxy_NativeObject.md), [SilhouetteCurves.AddSilhouette](../SilhouetteCurves/SilhouetteCurves_AddSilhouette.md), [SilhouetteCurves.Item](../SilhouetteCurves/SilhouetteCurves_Item.md)

## Derived Classes

[SilhouetteCurveProxy](../SilhouetteCurveProxy/SilhouetteCurveProxy.md)

## Version

Introduced in version 2012
