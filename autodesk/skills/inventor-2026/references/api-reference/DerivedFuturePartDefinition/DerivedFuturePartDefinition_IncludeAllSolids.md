# DerivedFuturePartDefinition.IncludeAllSolids Property

Parent Object: [DerivedFuturePartDefinition](../DerivedFuturePartDefinition/DerivedFuturePartDefinition.md)

## Description

Read-write property that defines whether all solids are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. If set to kDerivedIncludeAll, all solids will be included. If set to kDerivedExcludeAll, no solids will be included. If set to kDerivedIndividualDefined, then the inclusion state of each solid is defined by the solid itself. The available solids are accessed using the Solids property of the DerivedPartDefinition object.

## Syntax

DerivedFuturePartDefinition.**IncludeAllSolids**() As [DerivedComponentOptionEnum](../DerivedComponentOptionEnum.md)

## Property Value

This is a read/write property whose value is a [DerivedComponentOptionEnum](../DerivedComponentOptionEnum.md).

## Version

Introduced in version 2018
