# Matrix.SetTranslation Method

Parent Object: [Matrix](../Matrix/Matrix.md)

## Description

Sets the translation portion of the matrix. If the optional ResetRotation flag is True, the rotation portion of the matrix is reset to identity.

## Syntax

Matrix.**SetTranslation**( ***Translation*** As [Vector](../Vector/Vector.md), [***ResetRotation***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Translation | [Vector](../Vector/Vector.md) | Input Vector that specifies the new translation portion of the matrix. |
| ResetRotation | Boolean | Optional input Boolean that indicates whether to reset to rotation portion of the matrix to identity. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [InteractionGraphics](../../sample-programs/InteractionGraphics_Sample.md) | The sample creates overlay graphics. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Assembly Move Occurrence](../../sample-programs/TransformOccurrence_Sample.md) | This sample demonstrates moving a component occurrence. This sample performs a translate, but a rotate can also be performed since the transform is defined using a matrix. |
| [UCS by transformation matrix](../../sample-programs/UserCoordinateSystems_CreateDefinition_Sample.md) | This sample demonstrates the creation of a user coordinate system (UCS) by specifying a transformation matrix. |

## Version

Introduced in version 4
