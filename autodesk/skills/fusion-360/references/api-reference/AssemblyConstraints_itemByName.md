# AssemblyConstraints.itemByName Method![](../images/TestTubeLarge.png)

Parent Object: [AssemblyConstraints](AssemblyConstraints.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AssemblyConstraints.h>

## Description

Function that returns the specified assembly constraint object using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"assemblyConstraints\_var" is a variable referencing an [AssemblyConstraints](AssemblyConstraints.htm) object.```` ``` returnValue = assemblyConstraints_var.itemByName(name) ``` ```` |

"assemblyConstraints\_var" is a variable referencing an [AssemblyConstraints](AssemblyConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AssemblyConstraint](AssemblyConstraint.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the item within the collection to return. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |