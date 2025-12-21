# DerivedFutureAssemblyOccurrence.InclusionOption Property

Parent Object: [DerivedFutureAssemblyOccurrence](../DerivedFutureAssemblyOccurrence/DerivedFutureAssemblyOccurrence.md)

## Description

Read-write property that defines if this occurrence is included and if it is how it is used in the derived assembly. Valid values for this property are kDerivedIncludeAll, kDerivedExcludeAll and kDerivedIndividualDefined.

If this occurrence represents a subassembly, setting to kDerivedIncludeAll will cause all sub occurrences to add material to the solid body. If setting to kDerivedIndividualDefined, the sub occurrence’s define their behavior. An important distinction between “All” and “IndividualDefined” switches is that as occurrences are added to the subassembly they will automatically be included if any of the “All” switches are used. If the “InidividualDefined” switch is used, new components added to the assembly will be set to kDerivedExludeAll.
If this occurrence represents a leaf part, then valid options are kDerivedIncludeAll or kDerivedExcludeAll.

## Syntax

DerivedFutureAssemblyOccurrence.**InclusionOption**() As [DerivedComponentOptionEnum](../DerivedComponentOptionEnum.md)

## Property Value

This is a read/write property whose value is a [DerivedComponentOptionEnum](../DerivedComponentOptionEnum.md).

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |