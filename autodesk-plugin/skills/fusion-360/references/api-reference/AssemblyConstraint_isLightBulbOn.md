# AssemblyConstraint.isLightBulbOn Property![](../images/TestTubeLarge.png)

Parent Object: [AssemblyConstraint](AssemblyConstraint.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AssemblyConstraint.h>

## Description

Gets and sets if the light bulb of this assembly constraint, as displayed in the browser, is on or off. An assembly constraint will only be visible if the light bulb is switched on. However, the light bulb can be on and the assembly constraint still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the light bulb of the parent Joints folder is off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"assemblyConstraint\_var" is a variable referencing an AssemblyConstraint object. |

"assemblyConstraint\_var" is a variable referencing an AssemblyConstraint object. ```` ``` #include <Fusion/Components/AssemblyConstraint.h>  // Get the value of the property. boolean propertyValue = assemblyConstraint_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = assemblyConstraint_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |