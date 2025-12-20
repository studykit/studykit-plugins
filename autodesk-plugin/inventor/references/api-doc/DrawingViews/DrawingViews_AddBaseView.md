# DrawingViews.AddBaseView Method

Parent Object: [DrawingViews](../DrawingViews/DrawingViews.md)

## Description

Method that creates a new base . The newly created DrawingView is returned.

## Remarks

Valid values for the NameValue map of the AdditionalOptions argument is shown below:

| Name | Type | Valid Document Type | Notes |
| --- | --- | --- | --- |
| WeldmentFeatureGroup | Value from WeldmentFeatureGroupEnum | Weldment | kAssemblyFeatureGroup : General assembly group. kPreperationsFeatureGroup : Preparations group. kWeldsFeatureGroup : Welds group. kMachiningFeatureGroup : Machining group. |
| SheetMetalFoldedModel | Boolean | Sheet metal PartDocument | The part document must contain a flat pattern if a flat view (False) is specified. If a flat doesn't exist, a folded view will be created. |
| DesignViewRepresentation | String | Assembly | The name of the design view representation. |
| DesignViewAssociative | Boolean | Assembly | Indicates if the drawing view will be associative to the design view. A design view must be specified. |
| PositionalRepresentation | String | Assembly | The name of the positional representation. |
| MemberName | String | Part, Assembly | The name of the iPart or iAssembly member. |
| PresentationView | String | Presentation | The name of the presentation view. |
| PresentationViewAssociative | Boolean | Presentation | Indicates if the view should be associative to the presentation view. A presentation view must be specified |
| Include3DAnnotations | Boolean | Part, Assembly | Indicates if the 3D annotations should be included when create the drawing view. |

## Syntax

DrawingViews.**AddBaseView**( ***Model*** As [Document](../Document/Document.md), ***Position*** As [Point2d](../Point2d/Point2d.md), ***Scale*** As Double, ***ViewOrientation*** As [ViewOrientationTypeEnum](../ViewOrientationTypeEnum.md), ***ViewStyle*** As [DrawingViewStyleEnum](../DrawingViewStyleEnum.md), [***ModelViewName***] As String, [***ArbitraryCamera***] As Variant, [***AdditionalOptions***] As Variant ) As [DrawingView](../DrawingView/DrawingView.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Model | [Document](../Document/Document.md) | Input Document that specifies the document to create the view of. Valid document types include part file, assembly files, and presentation files. This method uses a Document object as input rather than a filename to allow the insertion of a document into a drawing and avoid the requirement of that document first being saved to a file. If a document already exists as a file on disk you can use the Documents.Open method to open the file and obtain a Document object. Typically, you'll want to set the OpenVisible argument of the Open method to False so the open is invisible to the user. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the placement point of the view on the sheet. |
| Scale | Double | Input Double that specifies the drawing view scale factor. |
| ViewOrientation | [ViewOrientationTypeEnum](../ViewOrientationTypeEnum.md) | Input ViewOrientationTypeEnum that specifies the orientation of the model within the view. If this value is kArbitraryViewOrientation the orientation is derived from the Camera specified by the ArbitraryCamera argument. |
| ViewStyle | [DrawingViewStyleEnum](../DrawingViewStyleEnum.md) | Input DrawingViewStyleEnum the specifies the display style of the geometry within the view. Valid values are kHiddenLineDrawingViewStyle, kHiddenLineRemovedDrawingViewStyle, kShadedDrawingViewStyle, and kShadedHiddenLineDrawingViewStyle. If kFromBaseDrawingViewStyle is specified, an error is returned. |
| ModelViewName | String | Optional input String that defines the design view name for assembly files, or the presentation view name for presentation files. This argument is ignored if the document type specified by the Model argument is a part file (.ipt). |
| ArbitraryCamera | Variant | Optional input Camera object that specifies the model orientation within the view. This argument is ignored if the ViewOrientation argument is not kArbitraryViewOrientation.   This is an optional argument whose default value is null. |
| AdditionalOptions | Variant | Optional input NameValueMap object that specifies additional or advanced options as described in the remarks section.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding Representation views](../../sample-programs/DrawingViews_AddBaseView_Sample.md) | This sample demonstrates how to create a base view by specifying various representations. |
| [Create flat pattern drawing view](../../sample-programs/DrawingViews_AddBaseView2_Sample.md) | This sample demonstrates the creation of a flat pattern base view in a drawing. |
| [Create base view with representations](../../sample-programs/DrawingViews_AddBaseView3_Sample.md) | This sample demonstrates how to create a base view by specifying various representations. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |