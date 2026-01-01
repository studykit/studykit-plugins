# FilletSetbackVertex Object

## Description

The FilletSetbackVertex object provides access to a vertex that is valid to define fillet setbacks for. It also provides access to the edges connected to the vertex and each edge's associated setback value.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [MinimalSetback](../FilletSetbackVertex/FilletSetbackVertex_MinimalSetback.md) | Gets and sets whether the minimum allowable setback should be used for this vertex. |
| [SetbackCount](../FilletSetbackVertex/FilletSetbackVertex_SetbackCount.md) | Property that returns the number of edges connected to the vertex. Each edge is represented by a FilletSetback object which can be obtained using the Setback property. |
| [SetbackItem](../FilletSetbackVertex/FilletSetbackVertex_SetbackItem.md) | Method that returns the specified FilletSetback object from this vertex. |
| [Type](../FilletSetbackVertex/FilletSetbackVertex_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseSetbacks](../FilletSetbackVertex/FilletSetbackVertex_UseSetbacks.md) | Gets and sets whether or not to use setback values. |
| [Vertex](../FilletSetbackVertex/FilletSetbackVertex_Vertex.md) | Property that gets the vertex shared by the edges. This property is only available when a FilletDefinition object is being defined to use as input for creating a fillet. When the parent FilletDefinition object is obtained from an existing Fillet, the end-of-part marker should be placed above this fillet feature to allow access this property. |

## Accessed From

[FilletDefinition.SetbackVertexItem](../FilletDefinition/FilletDefinition_SetbackVertexItem.md)

## Version

Introduced in version 5.3
