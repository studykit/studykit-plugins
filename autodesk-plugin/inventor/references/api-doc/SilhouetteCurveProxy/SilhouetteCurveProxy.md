# SilhouetteCurveProxy Object

Derived from: [SilhouetteCurve](../SilhouetteCurve/SilhouetteCurve.md) Object

## Description

SilhouetteCurveProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../SilhouetteCurveProxy/SilhouetteCurveProxy_BreakLink.md) | Method that breaks the link between the silhouette curve and the model. |
| [Delete](../SilhouetteCurveProxy/SilhouetteCurveProxy_Delete.md) | Method that deletes the silhouette curve. This will delete all of the related sketch entities. |
| [Edit](../SilhouetteCurveProxy/SilhouetteCurveProxy_Edit.md) | Method that edits all of the inputs used to compute the silhouette curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit. |
| [GetReferenceKey](../SilhouetteCurveProxy/SilhouetteCurveProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SilhouetteCurveProxy/SilhouetteCurveProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SilhouetteCurveProxy/SilhouetteCurveProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Body](../SilhouetteCurveProxy/SilhouetteCurveProxy_Body.md) | Read-write property that defines the surfaces the silhouette is calculated for. |
| [ContainingOccurrence](../SilhouetteCurveProxy/SilhouetteCurveProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DirectionEntity](../SilhouetteCurveProxy/SilhouetteCurveProxy_DirectionEntity.md) | Read-write property gets and set the direction used to calculate the silhouette curve. |
| [ExcludedFaces](../SilhouetteCurveProxy/SilhouetteCurveProxy_ExcludedFaces.md) | Read-write property that gets and sets the faces that are excluded in the silhouette curve projection. |
| [ExcludeInternalFaces](../SilhouetteCurveProxy/SilhouetteCurveProxy_ExcludeInternalFaces.md) | Read-write property that specifies whether to exclude the internal faces from the silhouette curve projection. |
| [ExcludeStraightFaces](../SilhouetteCurveProxy/SilhouetteCurveProxy_ExcludeStraightFaces.md) | Read-write property that specifies whether to exclude the faces that are perpendicular to the project direction from the silhouette curve projection. |
| [Name](../SilhouetteCurveProxy/SilhouetteCurveProxy_Name.md) | Property that gets and sets name of the silhouette curve. |
| [NativeObject](../SilhouetteCurveProxy/SilhouetteCurveProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../SilhouetteCurveProxy/SilhouetteCurveProxy_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SketchEntities](../SilhouetteCurveProxy/SilhouetteCurveProxy_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to silhouette curve. |
| [Type](../SilhouetteCurveProxy/SilhouetteCurveProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |