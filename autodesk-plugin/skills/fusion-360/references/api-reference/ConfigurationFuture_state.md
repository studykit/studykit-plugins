# ConfigurationFuture.state Property

Parent Object: [ConfigurationFuture](ConfigurationFuture.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFuture.h>

## Description

Returns the current state of the process associated with this future.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFuture\_var" is a variable referencing a ConfigurationFuture object. |

"configurationFuture\_var" is a variable referencing a ConfigurationFuture object. ```` ``` #include <Fusion/Configurations/ConfigurationFuture.h>  // Get the value of the property. FutureStates propertyValue = configurationFuture_var->state(); ``` ```` |

## Property Value

This is a read only property whose value is a [FutureStates](FutureStates.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |