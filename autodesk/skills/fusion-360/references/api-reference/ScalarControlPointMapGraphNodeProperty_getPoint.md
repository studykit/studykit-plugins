# ScalarControlPointMapGraphNodeProperty.getPoint Method![](../images/TestTubeLarge.png)

Parent Object: [ScalarControlPointMapGraphNodeProperty](ScalarControlPointMapGraphNodeProperty.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/ScalarControlPointMapGraphNodeProperty.h>

## Description

Get the point at index.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scalarControlPointMapGraphNodeProperty\_var" is a variable referencing a [ScalarControlPointMapGraphNodeProperty](ScalarControlPointMapGraphNodeProperty.htm) object.```` ``` returnValue = scalarControlPointMapGraphNodeProperty_var.getPoint(index) ``` ```` |

"scalarControlPointMapGraphNodeProperty\_var" is a variable referencing a [ScalarControlPointMapGraphNodeProperty](ScalarControlPointMapGraphNodeProperty.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ScalarControlPoint](ScalarControlPoint.htm) | The control point at this index. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | Index of the point to get. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |