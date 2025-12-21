# FlushConstraint.AffectedOccurrenceOne Property

Parent Object: [FlushConstraint](../FlushConstraint/FlushConstraint.md)

## Description

Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between.

## Syntax

FlushConstraint.**AffectedOccurrenceOne**() As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Property Value

This is a read only property whose value is a [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md).

## Version

Introduced in version 9
