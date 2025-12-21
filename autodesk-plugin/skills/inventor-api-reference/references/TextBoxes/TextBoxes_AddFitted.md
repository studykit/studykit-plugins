# TextBoxes.AddFitted Method

Parent Object: [TextBoxes](../TextBoxes/TextBoxes.md)

## Description

Method that creates a text box positioned at the specified point. The size of the resulting text box is just large enough to contain the input text.

## Syntax

TextBoxes.**AddFitted**( ***Position*** As [Point2d](../Point2d/Point2d.md), ***FormattedText*** As String, [***TextStyle***] As Variant ) As [TextBox](../TextBox/TextBox.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Position | [Point2d](../Point2d/Point2d.md) | Input that specifies the position of the text box. The position of this point in relation to the resulting text string is dependent on the vertical and horizontal justification of the text. For example if the vertical justification is the top and horizontal is the left, then the position point defines the upper\-left corner of the text box. If the vertical justification is the center and the horizontal justification is the center, the position point defines the center of the text box. |
| FormattedText | String | Input String that specifies the text of the text box. This string can contain tags that define internal formatting changes, which override the text style associated with the text box. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| TextStyle | Variant | Optional input Variant that specifies which text style to use for the text box. The text style can be specified by providing the name of an existing style or by supplying a TextStyle object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |
| [Extrude sketch text](../../sample-programs/ExtrudeFeatures_AddByDistanceExtent_Sample.md) | This sample demonstrates the creation of an extrude feature from sketch text. |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3
