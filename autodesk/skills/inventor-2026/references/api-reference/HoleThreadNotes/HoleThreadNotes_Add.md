# HoleThreadNotes.Add Method

Parent Object: [HoleThreadNotes](../HoleThreadNotes/HoleThreadNotes.md)

## Description

Method that creates a hole or thread note on the sheet. Different results are possible depending on the input provided, as discussed below.

## Remarks

In the example below there are three holes created using various modeling techniques. The top one was created using an extrude feature and a subsequent thread feature was added to it. The middle feature is a counter bore hole feature that is also tapped. The bottom feature is a standard hole.

![](../images/HoleThreadNotes_Add.png)

To get any of the four notes shown on the left-hand view the only required input is the Position to define the text position and a DrawingCurve defining which curve the note should point to. The text position is enough to determine where the note points to the circle. Notice that in the case of the thread feature you get a thread note if the input drawing curve is for the thread and you get a hole note if the drawing curve is for the hole. The right view demonstrates some other possibilities. The three circled notes can be created by defining the text position point, the geometry to point to and a point along that geometry. The geometry and point on the geometry are defined by providing a GeometryIntent object as input to the HoleOrThreadEdge argument. The other two notes in the right view require the input of the text position and one of the lines that represents the diameter of the thread. In addition, the LinearDiameterType argument must be set to True.

## Syntax

HoleThreadNotes.**Add**( ***Position*** As [Point2d](../Point2d/Point2d.md), ***HoleOrThreadEdge*** As Object, [***LinearDiameterType***] As Boolean, [***DimensionStyle***] As Variant ) As [HoleThreadNote](../HoleThreadNote/HoleThreadNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the position of the hole/thread note on the sheet. |
| HoleOrThreadEdge | Object | Input DrawingCurve or GeometryIntent object that specifies the edge to create the note for and the location along the edge the note points to. If the drawing curve or geometry intent does not represent a hole or thread edge, the method returns an error. See the discussion above for more information about how to get different results by providing different inputs for this argument. |
| LinearDiameterType | Boolean | Optional Input Boolean that specifies whether to create a leader type of note or a linear diameter type of note. There are two examples of linear diameter types in the figure above. These are the uncircled notes in the right view. The three circled notes illustrate a leader type of note. |
| DimensionStyle | Variant | Optional input Variant that specifies which dimension style to use for the note. The dimension style can be specified by providing the name of an existing style or by supplying a DimensionStyle object.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |

## Version

Introduced in version 2010
