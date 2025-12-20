# SinglePointRipTypeDef.GapSize Property

Parent Object: [SinglePointRipTypeDef](../SinglePointRipTypeDef/SinglePointRipTypeDef.md)

## Description

Property that returns the parameter controlling the width of the gap. When creating a new rip feature and the RipDefinition object is not associated with an actual feature, this property will return Nothing. You can use the SetSinglePointRipType method of the RipDefinition to set this value in that case. When this object is obtained from an existing rip feature you can edit the rip feature by modifying the parameter this property returns.

## Syntax

SinglePointRipTypeDef.**GapSize**() As [Parameter](../Parameter/Parameter.md)

## Property Value

This is a read only property whose value is a [Parameter](../Parameter/Parameter.md).

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |