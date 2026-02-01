# VolumetricCustomFeatures.createInput Method![](../images/TestTubeLarge.png)

Parent Object: [VolumetricCustomFeatures](VolumetricCustomFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VolumetricCustomFeatures.h>

## Description

Create a new VolumetricCustomFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"volumetricCustomFeatures\_var" is a variable referencing a [VolumetricCustomFeatures](VolumetricCustomFeatures.htm) object.```` ``` returnValue = volumetricCustomFeatures_var.createInput(boundaryBody) ``` ```` |

"volumetricCustomFeatures\_var" is a variable referencing a [VolumetricCustomFeatures](VolumetricCustomFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [VolumetricCustomFeatureInput](VolumetricCustomFeatureInput.htm) | Returns the newly created VolumetricCustomFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| boundaryBody | [Base](Base.htm) | The boundary body for the volumetric model. Must be a BRepBody or MeshBody. Must have the same parent component as the VolumetricCustomFeatures. |

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