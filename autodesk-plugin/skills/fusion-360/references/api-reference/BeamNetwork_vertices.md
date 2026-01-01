# BeamNetwork.vertices Property![](../images/TestTubeLarge.png)

Parent Object: [BeamNetwork](BeamNetwork.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/BeamNetwork.h>

## Description

The vertices of the beam network. Each vertex is a Point3D.

## Syntax

* [Python](#Python)
* [C++](#C++)

"beamNetwork\_var" is a variable referencing a BeamNetwork object. |

"beamNetwork\_var" is a variable referencing a BeamNetwork object. ```` ``` #include <Volume/Volumetric/BeamNetwork.h>  // Get the value of the property. std::vector<Ptr<Point3D>> propertyValue = beamNetwork_var->vertices();  // Set the value of the property, where value_var is a Point3D. bool returnValue = beamNetwork_var->vertices(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Point3D](Point3D.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |