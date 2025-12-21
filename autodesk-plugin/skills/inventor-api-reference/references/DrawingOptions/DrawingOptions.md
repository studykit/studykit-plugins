# DrawingOptions Object

## Description

The DrawingOptions object provides access to properties that provide read and write access of the drawing related application options. This is somewhat equivalent to the Drawing tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingOptions/DrawingOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArcDimensionType](../DrawingOptions/DrawingOptions_ArcDimensionType.md) | Gets/Sets the type of dimensioning to use while placing arc dimensions on drawing sheets. |
| [CenterDimensionText](../DrawingOptions/DrawingOptions_CenterDimensionText.md) | Gets/Sets the dimension text is to be centered when adding dimensions to drawing views. |
| [CircleDimensionType](../DrawingOptions/DrawingOptions_CircleDimensionType.md) | Gets/Sets the type of dimensioning to use while placing circle dimensions on drawing sheets. |
| [DefaultDrawingFileType](../DrawingOptions/DrawingOptions_DefaultDrawingFileType.md) | Gets/Sets the default file type (.idw or .dwg) to use when creating new drawings. |
| [DefaultLayerStyle](../DrawingOptions/DrawingOptions_DefaultLayerStyle.md) | Gets/Sets the default style to use for drawing layers. |
| [DefaultNonInventorDWGFileOpenBehavior](../DrawingOptions/DrawingOptions_DefaultNonInventorDWGFileOpenBehavior.md) | Gets/Sets the default file open behavior for non-Inventor DWG files. |
| [DefaultObjectStyle](../DrawingOptions/DrawingOptions_DefaultObjectStyle.md) | Gets/Sets the default style to use for drawing objects. |
| [DisplayLineWeights](../DrawingOptions/DrawingOptions_DisplayLineWeights.md) | Gets/Sets the display of unique line weights in drawings. |
| [EditDimensionWhenCreated](../DrawingOptions/DrawingOptions_EditDimensionWhenCreated.md) | Gets/Sets whether the edit dimension dialog should be shown when a dimension is created using the 'General Dimension' command. |
| [EnableBackgroundUpdates](../DrawingOptions/DrawingOptions_EnableBackgroundUpdates.md) | Gets/Sets whether drawing views are computed as a background process or not. |
| [EnableOrdinateDimGeomSelection](../DrawingOptions/DrawingOptions_EnableOrdinateDimGeomSelection.md) | Gets/Sets the selection of drawing geometry when creating ordinate dimensions. |
| [EnablePartModificationFromDrawing](../DrawingOptions/DrawingOptions_EnablePartModificationFromDrawing.md) | Enables/disables part modification from within a drawings. |
| [GetModelDimensions](../DrawingOptions/DrawingOptions_GetModelDimensions.md) | Gets/Sets the default for the dimensions option in the create view dialog boxes. |
| [InventorDWGFileVersion](../DrawingOptions/DrawingOptions_InventorDWGFileVersion.md) | Gets/Sets the AutoCAD DWG version for Inventor DWG files. |
| [LinearDimensionType](../DrawingOptions/DrawingOptions_LinearDimensionType.md) | Gets/Sets the type of dimensioning to use while placing linear dimensions on drawing sheets. |
| [LineWeightType](../DrawingOptions/DrawingOptions_LineWeightType.md) | Gets/Sets the type of line weight to apply when displaying lines in the drawing. |
| [ShowUncutSectionViewPreview](../DrawingOptions/DrawingOptions_ShowUncutSectionViewPreview.md) | Gets/Sets the section view previews should be displayed in uncut mode. |
| [StandardPartsSectionBehavior](../DrawingOptions/DrawingOptions_StandardPartsSectionBehavior.md) | Gets/Sets the sectioning behavior for standard parts when section views are created in the drawing. |
| [TitleBlockAlignment](../DrawingOptions/DrawingOptions_TitleBlockAlignment.md) | Gets/Sets the default title block location. |
| [Type](../DrawingOptions/DrawingOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpperLimitForFirstRangeOfLineWeights](../DrawingOptions/DrawingOptions_UpperLimitForFirstRangeOfLineWeights.md) | Gets/Sets the upper limit for the first range of line weights. |
| [UpperLimitForSecondRangeOfLineWeights](../DrawingOptions/DrawingOptions_UpperLimitForSecondRangeOfLineWeights.md) | Gets/Sets the upper limit for the second range of line weights. |
| [UpperLimitForThirdRangeOfLineWeights](../DrawingOptions/DrawingOptions_UpperLimitForThirdRangeOfLineWeights.md) | Gets/Sets the upper limit for the third range of line weights. |
| [ViewBlockInsertionPoint](../DrawingOptions/DrawingOptions_ViewBlockInsertionPoint.md) | Gets/Sets default insertion point for a view block. |
| [ViewJustification](../DrawingOptions/DrawingOptions_ViewJustification.md) | Gets/Sets the default drawing view justification. |
| [ViewPreview](../DrawingOptions/DrawingOptions_ViewPreview.md) | Gets/Sets the preview type for drawing views. |

## Accessed From

[Application.DrawingOptions](../Application/Application_DrawingOptions.md), [InventorServer.DrawingOptions](InventorServer_DrawingOptions.md), [InventorServerObject.DrawingOptions](InventorServerObject_DrawingOptions.md)

## Version

Introduced in version 2008
