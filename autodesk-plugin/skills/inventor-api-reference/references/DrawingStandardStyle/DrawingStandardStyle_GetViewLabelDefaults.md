# DrawingStandardStyle.GetViewLabelDefaults Method

Parent Object: [DrawingStandardStyle](../DrawingStandardStyle/DrawingStandardStyle.md)

## Description

Method that returns the drawing view label defaults for the specified view type.

## Syntax

DrawingStandardStyle.**GetViewLabelDefaults**( ***ViewType*** As [DrawingViewTypeEnum](../DrawingViewTypeEnum.md), ***Prefix*** As String, ***Visible*** As Boolean, ***FormattedText*** As String, ***ConstrainToBorder*** As Boolean, ***PlaceBelowView*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ViewType | [DrawingViewTypeEnum](../DrawingViewTypeEnum.md) | Input DrawingViewTypeEnum value that specifies the drawing view type for which to return the label defaults. |
| Prefix | String | Output String that returns the default view label prefix. |
| Visible | Boolean | Output Boolean that returns whether the label should be displayed by default. |
| FormattedText | String | Output String that returns the content of the view label. See the documentation of the DrawingViewLabel.FormattedText property for details, or see the list of XML text formatting tags under Reference Topics in the Overviews section. |
| ConstrainToBorder | Boolean | Output Boolean that returns whether the view label is constrained to the view. If a value of True is returned, the view label maintains its relative position to the view boundary as the boundary changes in size or position due to a modeling change, changing a view's assembly representation, or changing the view scale. |
| PlaceBelowView | Boolean | Output Boolean that returns whether to place the label below or above the drawing view. |

## Version

Introduced in version 2010
