# ProjectedCut Object

## Description

The ProjectedCut object represents a set of projected cut edges on the sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../ProjectedCut/ProjectedCut_BreakLink.md) | Method that breaks the link between the projected cut edges and the model. |
| [Delete](../ProjectedCut/ProjectedCut_Delete.md) | Method that deletes the projected cut edges. |
| [GetReferenceKey](../ProjectedCut/ProjectedCut_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProjectedCut/ProjectedCut_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ProjectedCut/ProjectedCut_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Name](../ProjectedCut/ProjectedCut_Name.md) | Gets and sets name of the projected cut edges. |
| [Parent](../ProjectedCut/ProjectedCut_Parent.md) | Property that returns the parent sketch of the projected cut edges. |
| [SketchEntities](../ProjectedCut/ProjectedCut_SketchEntities.md) | Property that returns a collection of sketch entities that belong to the projected cut edges. The sketch entities returned by this property cannot be edited or deleted because they are associated with the projected edges in the model. |
| [Type](../ProjectedCut/ProjectedCut_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ProjectedCutProxy.NativeObject](../ProjectedCutProxy/ProjectedCutProxy_NativeObject.md), [ProjectedCuts.Add](../ProjectedCuts/ProjectedCuts_Add.md), [ProjectedCuts.Item](../ProjectedCuts/ProjectedCuts_Item.md)

## Derived Classes

[ProjectedCutProxy](../ProjectedCutProxy/ProjectedCutProxy.md)

## Version

Introduced in version 2010
