# MarkStyle Object

## Description

MarkStyle object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../MarkStyle/MarkStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../MarkStyle/MarkStyle_Copy.md) | Method that creates a new local style object. |
| [Delete](../MarkStyle/MarkStyle_Delete.md) | Method that deletes this style object. |
| [GetBackCustomLineType](../MarkStyle/MarkStyle_GetBackCustomLineType.md) | Method that returns information regarding the custom line type in use. |
| [GetFrontCustomLineType](../MarkStyle/MarkStyle_GetFrontCustomLineType.md) | Method that returns information regarding the custom line type in use. |
| [GetReferenceKey](../MarkStyle/MarkStyle_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [GetStrokeFontList](../MarkStyle/MarkStyle_GetStrokeFontList.md) | Method that gets the array of strings containing the stroke font list. |
| [SaveToGlobal](../MarkStyle/MarkStyle_SaveToGlobal.md) | Method that saves this style to the global repository. |
| [SetBackCustomLineType](../MarkStyle/MarkStyle_SetBackCustomLineType.md) | Method that sets a the style to use custom line type from the specified .lin file. |
| [SetFrontCustomLineType](../MarkStyle/MarkStyle_SetFrontCustomLineType.md) | Method that sets a the style to use custom line type from the specified .lin file. |
| [UpdateFromGlobal](../MarkStyle/MarkStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MarkStyle/MarkStyle_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../MarkStyle/MarkStyle_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [BackLayerColor](../MarkStyle/MarkStyle_BackLayerColor.md) | Property that gets and sets the color for back Layer. |
| [BackLayerLineType](../MarkStyle/MarkStyle_BackLayerLineType.md) | Property that gets and sets the line type for back Layer. |
| [BackLayerLineWeight](../MarkStyle/MarkStyle_BackLayerLineWeight.md) | Property that gets and sets the line weight for back Layer. |
| [BackLayerName](../MarkStyle/MarkStyle_BackLayerName.md) | Property that gets and sets the layer name for back layer. |
| [FrontLayerColor](../MarkStyle/MarkStyle_FrontLayerColor.md) | Property that gets and sets the color for front Layer. |
| [FrontLayerLineType](../MarkStyle/MarkStyle_FrontLayerLineType.md) | Property that gets and sets the line type for front Layer. |
| [FrontLayerLineWeight](../MarkStyle/MarkStyle_FrontLayerLineWeight.md) | Property that gets and sets the line weight for front Layer. |
| [FrontLayerName](../MarkStyle/MarkStyle_FrontLayerName.md) | Property that gets and sets the layer name for front face. |
| [InternalName](../MarkStyle/MarkStyle_InternalName.md) | Property that returns the unique name of the style. |
| [InUse](../MarkStyle/MarkStyle_InUse.md) | Property that returns whether this style is in use. |
| [MarkDepthType](../MarkStyle/MarkStyle_MarkDepthType.md) | Property that gets and sets the mark depth type. |
| [MarkTextType](../MarkStyle/MarkStyle_MarkTextType.md) | Property that gets and sets the mark text type. |
| [Name](../MarkStyle/MarkStyle_Name.md) | Property that gets and sets the name of the style. |
| [Parent](../MarkStyle/MarkStyle_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [StrokesFontName](../MarkStyle/MarkStyle_StrokesFontName.md) | Property that gets and sets the mark text strokes font name. |
| [StyleLocation](../MarkStyle/MarkStyle_StyleLocation.md) | Gets the location status of the mark style. |
| [Type](../MarkStyle/MarkStyle_Type.md) | Gets the constant that indicates the type of this object. |
| [UpToDate](../MarkStyle/MarkStyle_UpToDate.md) | Read-only property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[MarkGeometrySet.Style](../MarkGeometrySet/MarkGeometrySet_Style.md), [MarkStyle.ConvertToLocal](../MarkStyle/MarkStyle_ConvertToLocal.md), [MarkStyle.Copy](../MarkStyle/MarkStyle_Copy.md), [MarkStylesEnumerator.Item](../MarkStylesEnumerator/MarkStylesEnumerator_Item.md), [PartDocument.ActiveMarkStyle](../PartDocument/PartDocument_ActiveMarkStyle.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mark feature creation sample](../../sample-programs/MarkFeatureCreationSample_Sample.md) | This sample demonstrates how to create a mark feature in part document. |

## Version

Introduced in version 2023
