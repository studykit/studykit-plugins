# SurfaceBodyDefinition.CreateTransientSurfaceBody Method

Parent Object: [SurfaceBodyDefinition](../SurfaceBodyDefinition/SurfaceBodyDefinition.md)

## Description

Method that creates a transient SurfaceBody object based on the B-Rep defined within this SurfaceBodyDefinition object.

## Syntax

SurfaceBodyDefinition.**CreateTransientSurfaceBody**( ***Errors*** As [NameValueMap](../NameValueMap/NameValueMap.md), [***Options***] As Variant ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Errors | [NameValueMap](../NameValueMap/NameValueMap.md) | Output NameValueMap that contains a list of any errors that occurred during the creation of the surface body. This list will be empty if no errors occurred. |
| Options | Variant | List of options to control certain behaviors during the creation of the surface body. The various options are listed below. \* **DoStitch** ' Boolean value that specifies if the faces should be stitched together to create a connected set of faces or a solid if they result in a completely closed volume. If this value is True or is not specified stitching will be attempted. A value of False indicates that no stitching is attempted and the defined topology is used. \* **MergeFaces** ' Boolean value that specifies if the analytic faces should be merged where possible. If this value is False or is not specified then no merging is done. A value of True indicates that faces should be merged. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2011
