# InsertConstraintProxy.AffectedOccurrenceTwo Property

Parent Object: [InsertConstraintProxy](../InsertConstraintProxy/InsertConstraintProxy.md)

## Description

Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between.

## Syntax

InsertConstraintProxy.**AffectedOccurrenceTwo**() As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Property Value

This is a read only property whose value is a [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md).

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |