# WorkPlanes.AddByPlaneAndOffset Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane that is parallel to the input plane at a specified distance in the specified direction. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByPlaneAndOffset**( ***Plane*** As Object, ***Offset*** As Variant, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Offset | Variant | Input Variant that defines the offset distance of the Plane. This can be a numeric value or a string. The offset distance of a work plane is always defined by a parameter. When a new work plane is created that requires a parameter, that parameter is automatically created when the work plane is created. If a numeric value is supplied the new parameter is set to the value specified. The input value is in centimeters. If a string is supplied this will be used as the expression for the newly created parameter and will be interpreted the same as if the user entered it in a dialog. This means if a value is specified without a unit qualifier it will default to the current document length unit. The following is a valid entry for the offset, assuming the parameter d2 already exists and defines a length, "d2 + 3 in." The sign of the value controls which side of the plane the offset is in. A positive value will be in the positive normal side of the plane. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |

## Version

Introduced in version 4
