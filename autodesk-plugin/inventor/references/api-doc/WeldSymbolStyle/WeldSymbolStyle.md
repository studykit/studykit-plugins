# WeldSymbolStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

WeldSymbolStyle object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../WeldSymbolStyle/WeldSymbolStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../WeldSymbolStyle/WeldSymbolStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../WeldSymbolStyle/WeldSymbolStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetBackingSymbolsFilter](../WeldSymbolStyle/WeldSymbolStyle_GetBackingSymbolsFilter.md) | Method that gets the backing symbol filter. |
| [GetContourSymbolFilterVariationType](../WeldSymbolStyle/WeldSymbolStyle_GetContourSymbolFilterVariationType.md) | Gets the variation type of a contour symbol filter. |
| [GetContourSymbolsFilter](../WeldSymbolStyle/WeldSymbolStyle_GetContourSymbolsFilter.md) | Method that gets the contour symbol filter. |
| [GetIdentificationLineCustomLineType](../WeldSymbolStyle/WeldSymbolStyle_GetIdentificationLineCustomLineType.md) | Gets information regarding the custom line type in use for identification line. |
| [GetReferenceKey](../WeldSymbolStyle/WeldSymbolStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetWeldingSymbolFilterVariationType](../WeldSymbolStyle/WeldSymbolStyle_GetWeldingSymbolFilterVariationType.md) | Gets the variation type of a welding symbol filter. |
| [GetWeldingSymbolsFilter](../WeldSymbolStyle/WeldSymbolStyle_GetWeldingSymbolsFilter.md) | Method that gets the welding symbol filter. |
| [SaveToGlobal](../WeldSymbolStyle/WeldSymbolStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [SetBackingSymbolsFilter](../WeldSymbolStyle/WeldSymbolStyle_SetBackingSymbolsFilter.md) | Method that sets the backing symbol filter. |
| [SetContourSymbolFilterVariationType](../WeldSymbolStyle/WeldSymbolStyle_SetContourSymbolFilterVariationType.md) | Sets the variation type of a contour symbol filter. |
| [SetContourSymbolsFilter](../WeldSymbolStyle/WeldSymbolStyle_SetContourSymbolsFilter.md) | Method that sets the contour symbol filter. |
| [SetIdentificationLineCustomLineType](../WeldSymbolStyle/WeldSymbolStyle_SetIdentificationLineCustomLineType.md) | Sets a custom line type to the identification line from the specified .lin file. |
| [SetWeldingSymbolFilterVariationType](../WeldSymbolStyle/WeldSymbolStyle_SetWeldingSymbolFilterVariationType.md) | Sets the variation type of a welding symbol filter. |
| [SetWeldingSymbolsFilter](../WeldSymbolStyle/WeldSymbolStyle_SetWeldingSymbolsFilter.md) | Method that sets the welding symbol filter. |
| [UpdateFromGlobal](../WeldSymbolStyle/WeldSymbolStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WeldSymbolStyle/WeldSymbolStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowSidePositionAbove](../WeldSymbolStyle/WeldSymbolStyle_ArrowSidePositionAbove.md) | Gets and sets whether the arrow side position if above or below the reference line. |
| [Comments](../WeldSymbolStyle/WeldSymbolStyle_Comments.md) | Gets and sets comments associated with the style. |
| [FieldFlagDirection](../WeldSymbolStyle/WeldSymbolStyle_FieldFlagDirection.md) | Gets and sets the field weld symbol flag direction. |
| [IdentificationLineOffset](../WeldSymbolStyle/WeldSymbolStyle_IdentificationLineOffset.md) | Gets and sets the distance between the identification line and weld symbol. |
| [IdentificationLinePlacement](../WeldSymbolStyle/WeldSymbolStyle_IdentificationLinePlacement.md) | Gets and sets the default identification line placement. |
| [IdentificationLineType](../WeldSymbolStyle/WeldSymbolStyle_IdentificationLineType.md) | Gets and sets the default identification line type. |
| [InternalName](../WeldSymbolStyle/WeldSymbolStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../WeldSymbolStyle/WeldSymbolStyle_InUse.md) | Property that indicates if this style is in use. |
| [JustifyTextToLeader](../WeldSymbolStyle/WeldSymbolStyle_JustifyTextToLeader.md) | Gets and sets whether justifies the text to leader or not. |
| [LeaderStyle](../WeldSymbolStyle/WeldSymbolStyle_LeaderStyle.md) | Gets and sets the leader style used for the weld symbol style. |
| [Name](../WeldSymbolStyle/WeldSymbolStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../WeldSymbolStyle/WeldSymbolStyle_Parent.md) | Property returning the parent of this object. |
| [StyleLocation](../WeldSymbolStyle/WeldSymbolStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../WeldSymbolStyle/WeldSymbolStyle_StyleType.md) | Gets the type of the style. |
| [SymbolSizeLinkToTextHeight](../WeldSymbolStyle/WeldSymbolStyle_SymbolSizeLinkToTextHeight.md) | Gets and sets whether the symbol size is linked to text height or not. |
| [SymbolSizeScaleFactor](../WeldSymbolStyle/WeldSymbolStyle_SymbolSizeScaleFactor.md) | Gets and sets the symbol size scale factor. Scale factor must be between 0.5 and 2.00. |
| [TextStyle](../WeldSymbolStyle/WeldSymbolStyle_TextStyle.md) | Gets and sets the text style used for the weld symbol style. |
| [Type](../WeldSymbolStyle/WeldSymbolStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../WeldSymbolStyle/WeldSymbolStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[DrawingWeldingSymbol.Style](../DrawingWeldingSymbol/DrawingWeldingSymbol_Style.md), [ObjectDefaultsStyle.WeldSymbolStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_WeldSymbolStyle.md), [WeldSymbolStylesEnumerator.Item](../WeldSymbolStylesEnumerator/WeldSymbolStylesEnumerator_Item.md)

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |