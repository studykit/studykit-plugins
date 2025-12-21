# ComponentOccurrenceProxy.SurfaceBodies Property

Parent Object: [ComponentOccurrenceProxy](../ComponentOccurrenceProxy/ComponentOccurrenceProxy.md)

## Description

Property that returns the SurfaceBodies collection for the occurrence. This property applies to occurrences that represent a part and provides access to the B-Rep of that part. The B-Rep queries will return coordinate data in the context of the component definition that served as the starting point to access the occurrence, which can also be accessed through the ContextDefinition property.

## Syntax

ComponentOccurrenceProxy.**SurfaceBodies**() As [SurfaceBodies](../SurfaceBodies/SurfaceBodies.md)

## Property Value

This is a read only property whose value is a [SurfaceBodies](../SurfaceBodies/SurfaceBodies.md).

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |