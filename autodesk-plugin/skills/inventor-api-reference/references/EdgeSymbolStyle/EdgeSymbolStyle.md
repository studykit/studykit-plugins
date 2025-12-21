# EdgeSymbolStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

EdgeSymbolStyle object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../EdgeSymbolStyle/EdgeSymbolStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../EdgeSymbolStyle/EdgeSymbolStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../EdgeSymbolStyle/EdgeSymbolStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../EdgeSymbolStyle/EdgeSymbolStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../EdgeSymbolStyle/EdgeSymbolStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../EdgeSymbolStyle/EdgeSymbolStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeSymbolStyle/EdgeSymbolStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Comments](../EdgeSymbolStyle/EdgeSymbolStyle_Comments.md) | Gets and sets comments associated with the style. |
| [InternalName](../EdgeSymbolStyle/EdgeSymbolStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../EdgeSymbolStyle/EdgeSymbolStyle_InUse.md) | Property that indicates if this style is in use. |
| [LeaderStyle](../EdgeSymbolStyle/EdgeSymbolStyle_LeaderStyle.md) | Read-write property that gets and sets the leader style used for the edge symbol style. |
| [Name](../EdgeSymbolStyle/EdgeSymbolStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../EdgeSymbolStyle/EdgeSymbolStyle_Parent.md) | Property returning the parent of this object. |
| [StyleLocation](../EdgeSymbolStyle/EdgeSymbolStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../EdgeSymbolStyle/EdgeSymbolStyle_StyleType.md) | Gets the type of the style. |
| [TextStyle](../EdgeSymbolStyle/EdgeSymbolStyle_TextStyle.md) | Read-write property that gets and sets the text style used for the edge symbol style. |
| [Type](../EdgeSymbolStyle/EdgeSymbolStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../EdgeSymbolStyle/EdgeSymbolStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[EdgeSymbolDefinition.Style](../EdgeSymbolDefinition/EdgeSymbolDefinition_Style.md), [EdgeSymbolStylesEnumerator.Item](../EdgeSymbolStylesEnumerator/EdgeSymbolStylesEnumerator_Item.md), [ObjectDefaultsStyle.EdgeSymbolStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_EdgeSymbolStyle.md)

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |