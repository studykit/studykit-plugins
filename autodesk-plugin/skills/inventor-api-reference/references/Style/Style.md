# Style Object

## Description

The Style object is the base class for all the drawing styles and contains methods/properties common to all the styles.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../Style/Style_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../Style/Style_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../Style/Style_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../Style/Style_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../Style/Style_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../Style/Style_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Style/Style_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Comments](../Style/Style_Comments.md) | Gets and sets comments associated with the style. |
| [InternalName](../Style/Style_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../Style/Style_InUse.md) | Property that indicates if this style is in use. |
| [Name](../Style/Style_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../Style/Style_Parent.md) | Property returning the parent of this object. |
| [StyleLocation](../Style/Style_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../Style/Style_StyleType.md) | Gets the type of the style. |
| [Type](../Style/Style_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../Style/Style_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[BalloonStyle.ConvertToLocal](../BalloonStyle/BalloonStyle_ConvertToLocal.md), [BalloonStyle.Copy](../BalloonStyle/BalloonStyle_Copy.md), [CentermarkStyle.ConvertToLocal](../CentermarkStyle/CentermarkStyle_ConvertToLocal.md), [CentermarkStyle.Copy](../CentermarkStyle/CentermarkStyle_Copy.md), [DimensionStyle.ConvertToLocal](../DimensionStyle/DimensionStyle_ConvertToLocal.md), [DimensionStyle.Copy](../DimensionStyle/DimensionStyle_Copy.md), [DrawingStandardStyle.ConvertToLocal](../DrawingStandardStyle/DrawingStandardStyle_ConvertToLocal.md), [DrawingStandardStyle.Copy](../DrawingStandardStyle/DrawingStandardStyle_Copy.md), [EdgeSymbolStyle.ConvertToLocal](../EdgeSymbolStyle/EdgeSymbolStyle_ConvertToLocal.md), [EdgeSymbolStyle.Copy](../EdgeSymbolStyle/EdgeSymbolStyle_Copy.md), [FeatureControlFrameStyle.ConvertToLocal](../FeatureControlFrameStyle/FeatureControlFrameStyle_ConvertToLocal.md), [FeatureControlFrameStyle.Copy](../FeatureControlFrameStyle/FeatureControlFrameStyle_Copy.md), [HoleTableStyle.ConvertToLocal](../HoleTableStyle/HoleTableStyle_ConvertToLocal.md), [HoleTableStyle.Copy](../HoleTableStyle/HoleTableStyle_Copy.md), [Layer.ConvertToLocal](../Layer/Layer_ConvertToLocal.md), [Layer.Copy](../Layer/Layer_Copy.md), [LeaderStyle.ConvertToLocal](../LeaderStyle/LeaderStyle_ConvertToLocal.md), [LeaderStyle.Copy](../LeaderStyle/LeaderStyle_Copy.md), [ObjectDefaultsStyle.ConvertToLocal](../ObjectDefaultsStyle/ObjectDefaultsStyle_ConvertToLocal.md), [ObjectDefaultsStyle.Copy](../ObjectDefaultsStyle/ObjectDefaultsStyle_Copy.md), [PartsListStyle.ConvertToLocal](../PartsListStyle/PartsListStyle_ConvertToLocal.md), [PartsListStyle.Copy](../PartsListStyle/PartsListStyle_Copy.md), [RevisionTableStyle.ConvertToLocal](../RevisionTableStyle/RevisionTableStyle_ConvertToLocal.md), [RevisionTableStyle.Copy](../RevisionTableStyle/RevisionTableStyle_Copy.md), [SheetMetalStyle.ConvertToLocal](../SheetMetalStyle/SheetMetalStyle_ConvertToLocal.md), [SheetMetalStyle.Copy](../SheetMetalStyle/SheetMetalStyle_Copy.md), [Style.ConvertToLocal](../Style/Style_ConvertToLocal.md), [Style.Copy](../Style/Style_Copy.md), [Styles.Item](../Styles/Styles_Item.md), [SurfaceTextureStyle.ConvertToLocal](../SurfaceTextureStyle/SurfaceTextureStyle_ConvertToLocal.md), [SurfaceTextureStyle.Copy](../SurfaceTextureStyle/SurfaceTextureStyle_Copy.md), [TableStyle.ConvertToLocal](../TableStyle/TableStyle_ConvertToLocal.md), [TableStyle.Copy](../TableStyle/TableStyle_Copy.md), [TextStyle.ConvertToLocal](../TextStyle/TextStyle_ConvertToLocal.md), [TextStyle.Copy](../TextStyle/TextStyle_Copy.md), [TransitionSymbolStyle.ConvertToLocal](../TransitionSymbolStyle/TransitionSymbolStyle_ConvertToLocal.md), [TransitionSymbolStyle.Copy](../TransitionSymbolStyle/TransitionSymbolStyle_Copy.md), [UnfoldMethod.ConvertToLocal](../UnfoldMethod/UnfoldMethod_ConvertToLocal.md), [UnfoldMethod.Copy](../UnfoldMethod/UnfoldMethod_Copy.md), [ViewAnnotationStyle.ConvertToLocal](../ViewAnnotationStyle/ViewAnnotationStyle_ConvertToLocal.md), [ViewAnnotationStyle.Copy](../ViewAnnotationStyle/ViewAnnotationStyle_Copy.md), [WeldSymbolStyle.ConvertToLocal](../WeldSymbolStyle/WeldSymbolStyle_ConvertToLocal.md), [WeldSymbolStyle.Copy](../WeldSymbolStyle/WeldSymbolStyle_Copy.md)

## Derived Classes

[BalloonStyle](../BalloonStyle/BalloonStyle.md), [CentermarkStyle](../CentermarkStyle/CentermarkStyle.md), [DimensionStyle](../DimensionStyle/DimensionStyle.md), [DrawingStandardStyle](../DrawingStandardStyle/DrawingStandardStyle.md), [EdgeSymbolStyle](../EdgeSymbolStyle/EdgeSymbolStyle.md), [FeatureControlFrameStyle](../FeatureControlFrameStyle/FeatureControlFrameStyle.md), [HoleTableStyle](../HoleTableStyle/HoleTableStyle.md), [Layer](../Layer/Layer.md), [LeaderStyle](../LeaderStyle/LeaderStyle.md), [ObjectDefaultsStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle.md), [PartsListStyle](../PartsListStyle/PartsListStyle.md), [RevisionTableStyle](../RevisionTableStyle/RevisionTableStyle.md), [SheetMetalStyle](../SheetMetalStyle/SheetMetalStyle.md), [SurfaceTextureStyle](../SurfaceTextureStyle/SurfaceTextureStyle.md), [TableStyle](../TableStyle/TableStyle.md), [TextStyle](../TextStyle/TextStyle.md), [TransitionSymbolStyle](../TransitionSymbolStyle/TransitionSymbolStyle.md), [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md), [ViewAnnotationStyle](../ViewAnnotationStyle/ViewAnnotationStyle.md), [WeldSymbolStyle](../WeldSymbolStyle/WeldSymbolStyle.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |