# ModelDatums.CreateDefinition Method

Parent Object: [ModelDatums](../ModelDatums/ModelDatums.md)

## Description

Method that creates a model datum definition.

## Syntax

ModelDatums.**CreateDefinition**( ***DatumTargetPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***DatumTargetPlanes***] As Variant, [***DatumTargetTextPositions***] As Variant, [***DatumTargetIndices***] As Variant, [***DatumTargetType***] As Variant, [***DatumTargetAreaValueOne***] As Variant, [***DatumTargetAreaValueTwo***] As Variant, [***DatumText***] As Variant ) As [ModelDatumDefinition](../ModelDatumDefinition/ModelDatumDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DatumTargetPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection including the points that define the datum target points.  Valid entities for the datum target points are:  * WorkPoint * SketchPoint(the SketchPoint should be on the sketch that was created from a planar Face) * GeometryIntent (When GeometryIntent is provided, the point should be on a planar Face. The GeometryIntent object can be created using the CreateGeometryIntent method on the PartComponentDefinition or AssemblyComponentDefinition object.).  When provide the datum target points base on WorkPoint, the WorkPoint objects can not be on the same plane, and no datum target points base on other type of object can be provided. When provide the datum target points base on planar Face, all the datum target points should attach to the same Face or the Faces that are coplanar and from the same feature. When provide SketchPoint as datum target points they should be from the same planar sketch and the sketch should depend on a planar Face. |
| DatumTargetPlanes | Variant | Optional input ObjectCollection including the AnnotationPlaneDefinition objects that define the datum target planes that control the datum target texts’ orientation.   This is an optional argument whose default value is null. |
| DatumTargetTextPositions | Variant | Optional input ObjectCollection including the Point objects that define the datum target texts’ positions.   This is an optional argument whose default value is null. |
| DatumTargetIndices | Variant | Optional input Long array to specify the indices of the datum targets. The item count of this array should be the same as the item count of the DatumTargetPoints.   This is an optional argument whose default value is null. |
| DatumTargetType | Variant | Optional input the ModelDatumTargetTypeEnum that specifies the datum target type. If not specified the default ModelDatumTargetTypePoint is used.   This is an optional argument whose default value is null. |
| DatumTargetAreaValueOne | Variant | Optional input Double array that specifies the datum target area size. If not specified the default values will be used. If the DatumTargetType is specified as kModelDatumTargetTypeCircle the values indicate the area diameter, If the DatumTargetType is kModelDatumTargetTypeRectangle the values indicate the area width. For other DatumTargetType values this is ignored.   This is an optional argument whose default value is null. |
| DatumTargetAreaValueTwo | Variant | Optional input Double array that specifies the datum target area size. If not specified the default values will be used. If the DatumTargetType is specified as kModelDatumTargetTypeRectangle the values indicate the area height. For other DatumTargetType values this is ignored.   This is an optional argument whose default value is null. |
| DatumText | Variant | Optional input String that specifies the datum label. If not specified an available label will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2023
