# ConfigurationFuture.isValid Property

Parent Object: [ConfigurationFuture](ConfigurationFuture.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFuture.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFuture\_var" is a variable referencing a ConfigurationFuture object. |

"configurationFuture\_var" is a variable referencing a ConfigurationFuture object. ```` ``` #include <Fusion/Configurations/ConfigurationFuture.h>  // Get the value of the property. boolean propertyValue = configurationFuture_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |