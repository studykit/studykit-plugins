# DrawingStandardStyle.SetViewLabelDefaults Method

Parent Object: [DrawingStandardStyle](../DrawingStandardStyle/DrawingStandardStyle.md)

## Description

Method that sets the drawing view label defaults for the specified view type.

## Syntax

DrawingStandardStyle.**SetViewLabelDefaults**( ***ViewType*** As [DrawingViewTypeEnum](../DrawingViewTypeEnum.md), ***Prefix*** As String, ***Visible*** As Boolean, ***FormattedText*** As String, ***ConstrainToBorder*** As Boolean, ***PlaceBelowView*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewType | [DrawingViewTypeEnum](../DrawingViewTypeEnum.md) | Input DrawingViewTypeEnum value that specifies the drawing view type for which to set the label defaults. |
| Prefix | String | Input String that specifies the default view label prefix. |
| Visible | Boolean | Input Boolean that specifies whether the label should be displayed by default. |
| FormattedText | String | Input String that sets the content of the view label. See the documentation of the DrawingViewLabel.FormattedText property for details, or see the list of XML text formatting tags under Reference Topics in the Overviews section. |
| ConstrainToBorder | Boolean | Input Boolean that specifies whether the view label is constrained to the view. If set to True, the view label maintains its relative position to the view boundary as the boundary changes in size or position due to a modeling change, changing a view's assembly representation, or changing the view scale. |
| PlaceBelowView | Boolean | Input Boolean that specifies whether to place the label below or above the drawing view. |

## Version

Introduced in version 2010
