# AssemblyJointProxy.AffectedOccurrenceTwo Property

Parent Object: [AssemblyJointProxy](../AssemblyJointProxy/AssemblyJointProxy.md)

## Description

Read-only property that returns the second of the two occurrences affected by this joint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this joint is between.

## Syntax

AssemblyJointProxy.**AffectedOccurrenceTwo**() As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Property Value

This is a read only property whose value is a [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md).

## Version

Introduced in version 2014
