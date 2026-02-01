# GraphNodeProperties.itemByName Method![](../images/TestTubeLarge.png)

Parent Object: [GraphNodeProperties](GraphNodeProperties.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/GraphNodeProperties.h>

## Description

Returns the property with the specified internal name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphNodeProperties\_var" is a variable referencing a [GraphNodeProperties](GraphNodeProperties.htm) object.```` ``` returnValue = graphNodeProperties_var.itemByName(propertyName) ``` ```` |

"graphNodeProperties\_var" is a variable referencing a [GraphNodeProperties](GraphNodeProperties.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [GraphNodeProperty](GraphNodeProperty.htm) | Returns the specified property or null in the case where there is no property with the specified id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| propertyName | string | The id of the property. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Volumetric Custom Feature API Sample](VolumetricCustomFeatureSample_Sample.htm) | Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.  To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.  The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |