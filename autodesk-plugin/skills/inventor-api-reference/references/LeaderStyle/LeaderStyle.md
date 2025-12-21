# LeaderStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The LeaderStyle object represents a leader style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../LeaderStyle/LeaderStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../LeaderStyle/LeaderStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../LeaderStyle/LeaderStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetCustomLineType](../LeaderStyle/LeaderStyle_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../LeaderStyle/LeaderStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../LeaderStyle/LeaderStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [SetCustomLineType](../LeaderStyle/LeaderStyle_SetCustomLineType.md) | Method that sets a custom line type to the style from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [UpdateFromGlobal](../LeaderStyle/LeaderStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllAroundSymbolDiameter](../LeaderStyle/LeaderStyle_AllAroundSymbolDiameter.md) | Property that gets and sets the size of the all-around symbol for Feature Control Frames, Surface symbols, and Weld symbols (circular only). This value is used only if the ScaleToTextHeight property is set to False. |
| [Application](../LeaderStyle/LeaderStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadHeight](../LeaderStyle/LeaderStyle_ArrowheadHeight.md) | Property that gets and sets the height of the arrowhead relative to the associated line. |
| [ArrowheadSize](../LeaderStyle/LeaderStyle_ArrowheadSize.md) | Property that gets and sets the size of the arrowhead (i.e. the terminator). The value is that of width of the arrow if the terminator is an arrowhead or for diameter if the terminator is a circle. |
| [ArrowheadType](../LeaderStyle/LeaderStyle_ArrowheadType.md) | Property that gets and sets the arrowhead style to use. |
| [Color](../LeaderStyle/LeaderStyle_Color.md) | Property that gets and sets the color for the style. Setting the property to Nothing restores the style to the color defined by the layer. |
| [Comments](../LeaderStyle/LeaderStyle_Comments.md) | Gets and sets comments associated with the style. |
| [ExtensionLineOffset](../LeaderStyle/LeaderStyle_ExtensionLineOffset.md) | Property that gets and sets the space from the end of the edge to which the leader attaches to the beginning of the leader extension line. |
| [ExtensionLineOvershoot](../LeaderStyle/LeaderStyle_ExtensionLineOvershoot.md) | Property that gets and sets the length of the leader extension line past the end of the terminator. |
| [InternalName](../LeaderStyle/LeaderStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../LeaderStyle/LeaderStyle_InUse.md) | Property that indicates if this style is in use. |
| [LineType](../LeaderStyle/LeaderStyle_LineType.md) | Property that gets and sets the line type override. Setting the property to kDefaultLineType restores the default line type. If the property returns kCustomLineType, the GetCustomLineType method can be used to get further details about the line type. |
| [LineWeight](../LeaderStyle/LeaderStyle_LineWeight.md) | Property that gets and sets the thickness of this primitive/object. If LineDefinitionSpace is set to kScreenSpace, this value is defined in pixels. If LineDefinitionSpace is set to kModelSpace, this value is defined in model units (centimeters). |
| [Name](../LeaderStyle/LeaderStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../LeaderStyle/LeaderStyle_Parent.md) | Property returning the parent of this object. |
| [ScaleToTextHeight](../LeaderStyle/LeaderStyle_ScaleToTextHeight.md) | Property that gets and sets whether to define the all-around symbol size by the height of text from the symbol's text style. This specifies the size of the all-around symbol for Feature Control Frames, Surface symbols, and Weld symbols (circular only). |
| [StyleLocation](../LeaderStyle/LeaderStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../LeaderStyle/LeaderStyle_StyleType.md) | Gets the type of the style. |
| [Type](../LeaderStyle/LeaderStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../LeaderStyle/LeaderStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[BalloonStyle.AlternateLeaderStyle](../BalloonStyle/BalloonStyle_AlternateLeaderStyle.md), [BalloonStyle.LeaderStyle](../BalloonStyle/BalloonStyle_LeaderStyle.md), [DimensionStyle.LeaderStyle](../DimensionStyle/DimensionStyle_LeaderStyle.md), [EdgeSymbolStyle.LeaderStyle](../EdgeSymbolStyle/EdgeSymbolStyle_LeaderStyle.md), [FeatureControlFrameStyle.LeaderStyle](../FeatureControlFrameStyle/FeatureControlFrameStyle_LeaderStyle.md), [LeaderStylesEnumerator.Item](../LeaderStylesEnumerator/LeaderStylesEnumerator_Item.md), [ObjectDefaultsStyle.OriginIndicatorStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_OriginIndicatorStyle.md), [ObjectDefaultsStyle.SketchedSymbolLeaderStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_SketchedSymbolLeaderStyle.md), [OriginIndicator.LeaderStyle](../OriginIndicator/OriginIndicator_LeaderStyle.md), [RevisionTableStyle.RevisionTagLeaderStyle](../RevisionTableStyle/RevisionTableStyle_RevisionTagLeaderStyle.md), [SketchedSymbol.LeaderStyle](../SketchedSymbol/SketchedSymbol_LeaderStyle.md), [SurfaceTextureStyle.LeaderStyle](../SurfaceTextureStyle/SurfaceTextureStyle_LeaderStyle.md), [TransitionSymbolStyle.LeaderStyleForEdgeSelected](../TransitionSymbolStyle/TransitionSymbolStyle_LeaderStyleForEdgeSelected.md), [TransitionSymbolStyle.LeaderStyleForFaceSelected](../TransitionSymbolStyle/TransitionSymbolStyle_LeaderStyleForFaceSelected.md), [WeldSymbolStyle.LeaderStyle](../WeldSymbolStyle/WeldSymbolStyle_LeaderStyle.md)

## Version

Introduced in version 2009
