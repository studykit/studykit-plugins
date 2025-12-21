# SurfaceTextureStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The SurfaceTextureStyle object represents a surface texture style in a drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../SurfaceTextureStyle/SurfaceTextureStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../SurfaceTextureStyle/SurfaceTextureStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../SurfaceTextureStyle/SurfaceTextureStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../SurfaceTextureStyle/SurfaceTextureStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../SurfaceTextureStyle/SurfaceTextureStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../SurfaceTextureStyle/SurfaceTextureStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SurfaceTextureStyle/SurfaceTextureStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AvailableLaySymbols](../SurfaceTextureStyle/SurfaceTextureStyle_AvailableLaySymbols.md) | Gets and sets a bit mask defining the machining lay symbols to be made available for surface texture symbol creation. |
| [AvailableProfileDirectionSymbols](../SurfaceTextureStyle/SurfaceTextureStyle_AvailableProfileDirectionSymbols.md) | Gets and sets a bit mask defining the profile direction symbols to be made available for surface texture symbol creation. |
| [Comments](../SurfaceTextureStyle/SurfaceTextureStyle_Comments.md) | Gets and sets comments associated with the style. |
| [EnableAllAroundSymbol](../SurfaceTextureStyle/SurfaceTextureStyle_EnableAllAroundSymbol.md) | Gets and sets whether to enable the all-around indicator to the symbol. |
| [InternalName](../SurfaceTextureStyle/SurfaceTextureStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../SurfaceTextureStyle/SurfaceTextureStyle_InUse.md) | Property that indicates if this style is in use. |
| [LeaderStyle](../SurfaceTextureStyle/SurfaceTextureStyle_LeaderStyle.md) | Gets and sets the leader style used for a surface texture symbol. |
| [MachiningProhibitedSymbolSizeSmall](../SurfaceTextureStyle/SurfaceTextureStyle_MachiningProhibitedSymbolSizeSmall.md) | Gets and sets whether to use a large or small maching-prohibited symbol. If the property is set to True, the symbol with the smaller diameter is used. |
| [MajorityType](../SurfaceTextureStyle/SurfaceTextureStyle_MajorityType.md) | Gets and sets the majority type of this style. |
| [Name](../SurfaceTextureStyle/SurfaceTextureStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../SurfaceTextureStyle/SurfaceTextureStyle_Parent.md) | Property returning the parent of this object. |
| [StandardReferenceType](../SurfaceTextureStyle/SurfaceTextureStyle_StandardReferenceType.md) | Gets and sets the drafting standard that controls surface texture symbol format. |
| [StyleLocation](../SurfaceTextureStyle/SurfaceTextureStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../SurfaceTextureStyle/SurfaceTextureStyle_StyleType.md) | Gets the type of the style. |
| [TextStyle](../SurfaceTextureStyle/SurfaceTextureStyle_TextStyle.md) | Gets and sets the text style used to format the text in a surface texture symbol. |
| [Type](../SurfaceTextureStyle/SurfaceTextureStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../SurfaceTextureStyle/SurfaceTextureStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[ObjectDefaultsStyle.SurfaceTextureStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_SurfaceTextureStyle.md), [SurfaceTextureStylesEnumerator.Item](../SurfaceTextureStylesEnumerator/SurfaceTextureStylesEnumerator_Item.md), [SurfaceTextureSymbol.Style](../SurfaceTextureSymbol/SurfaceTextureSymbol_Style.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |