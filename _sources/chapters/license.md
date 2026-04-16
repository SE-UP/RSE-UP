#  Software Licenses

Generaly, licenses define how project materials (software, data, documents, etc.) can be used and redistributed.
If the license or a publication agreement makes it difficult for people to contribute, the project is less likely to attract new members, 
so the choice of license is crucial to the project's long-term sustainability.

> **Open Except...**
>
> Projects that are only developing software may not have any problem making everything open.
> Teams working with sensitive data, on the other hand,
> must be careful to ensure that what should be private isn't inadvertently shared.
> In particular,
> people who are new to Git (and even people who aren't)
> occasionally add raw data files containing personal identifying information to repositories.
> It's possible to rewrite the project's history to remove things when this happens,
> but that doesn't automatically erase copies people may have in forked repositories.

Every creative work has some sort of license;
the only question is whether authors and users know what it is and choose to enforce it.
Choosing a license for a project can be complex,
not least because the law hasn't kept up with everyday practice.
{cite:p}`Mori2012` and {cite:p}`Vand2014` are good starting points
to understand licensing and intellectual property from a researcher's point of view, while {cite:p}`Lind2008` is a deeper dive for those who want details.
Depending on country, institution, and job role, most creative works are automatically eligible for intellectual property protection.
However, members of the team may have different levels of copyright protection.
For example, students and faculty may have a copyright on the research work they produce, but university staff members may not, since their employment agreement may state that what they create on the job belongs to their employer.

To avoid legal messiness, every project should include an explicit license.
This license should be chosen early, since changing a license can be complicated. For example, each collaborator may hold copyright on their work
and therefore need to be asked for approval when a license is changed.
Similarly, changing a license does not change it retroactively,
so different users may wind up operating under different licensing structures.

> **Leave It to the Professionals**
>
> Don't write your own license.
> Legalese is a highly technical language,
> and words don't mean what you think they do.

To make license selection for code as easy as possible,
GitHub allows us to select one of several common software licenses when creating a repository.
The Open Source Initiative maintains [a list](https://opensource.org/licenses) of **open licenses**,
and [choosealicense.com](https://choosealicense.com/) will help us find a license that suits our needs. Some of the things we need to think about are:

1.  Do we want to license the work at all?
2.  Is the content we are licensing source code?
3.  Do we require people distributing derivative works to also distribute their code?
4.  Do we want to address patent rights?
5.  Is our license compatible with the licenses of the software we depend on?
6.  Do our institutions have any policies that may overrule our choices?
7.  Are there any copyright experts within our institution who can assist us?

Unfortunately, GitHub's list does not include common licenses for data or written works like papers and reports. 
Those can be added in manually, but it's often hard to understand the interactions among multiple licenses on different kinds of material {cite:p}`Alme2017`.

Just as the project's Code of Conduct is usually placed in a root-level file called `CONDUCT.md`, its license is usually put in a file called `LICENSE.md` that is also in the project's root directory.

## Licenses

Software licenses are crucial tools for both creators and users, they can be outlined as follows:

**Software as Intellectual Property**:

Like artwork, designs, and texts, software is considered intellectual property, a creation of the human mind deserving legal protection. This protection prevents unauthorized use and copying, giving creators control over their work.

**Common Forms of Protection**:

Copyright is the primary form of legal protection for software, safeguarding its code and functionality. Other relevant forms include patents (for unique algorithms or processes) and trade secrets (for confidential information).

**Software Licenses: Contracts for Use**:

A software license acts as a legal agreement between the owner (licensor) and the user (licensee). It grants permission to use the software under specific terms and conditions outlined in the agreement.

**What Licenses Define**:

Licenses typically specify: 

- The number of permitted installations.
- Commercial or non-commercial use allowed.
- Modification or distribution rights.
- Warranties and liabilities of the licensor.

**Importance of Licenses**:

Without a license, using copyrighted software is illegal. Licenses ensure legal and ethical use, protecting both creators and users.


There are numerous types of software licenses, ranging from free and open-source (e.g., GNU GPL) to paid commercial licenses with varying restrictions.
Understanding license terms is crucial before installing or using any software.
Breaching license terms can have legal consequences.

It is important think of Licenses when working with software, since they are vital for responsible and legal software use. Always take the time to read and understand the terms before using any software!

Fortunately, while there are a lot of different software licenses, there are only a few standard ones used.

### Types of software licenses

In general, there are three types of licenses.

#### Permissive licenses:
Allow users to use, modify, and distribute the work under certain conditions. They typically have few restrictions and allow for combination with other licenses.

#### Copyleft licenses:
Require that derivative works or modifications of the work be distributed under the same license terms. They aim to ensure that any improvements or modifications made to the work remain freely available to the community.

#### Proprietary licenses: 
Grant limited rights to use the work under specific conditions defined by the owner. These licenses usually restrict the redistribution, and modification of the work, or reverse engineering in case of software.

### Software and Data licenses 

Both are relevant in the context of research. However, data and software tend to use similar yet different licenses. The distinction arises from the inherent differences in their nature and the legal considerations associated with them, such as:

- Software is creative work, data is factual information

- Software is subject to copyright law, data may also be subject to privacy laws (sensitive data)

- Software licenses govern usage, modification and distribution of source code or executables.
 
- Data licenses address questions of access, usage, and sharing. 

- Practices continue to evolve in both domains.


### Common Open Source Software Licenses

#### MIT License:

The MIT License is widely known for its simplicity and permissiveness. It allows users to use, copy, modify, merge, publish, distribute, sublicense, and even sell copies of derivative software, so long as the original license and copyright notice are included. Because this license imposes that few restrictions, it encourages both academic sharing as well as commercial use. It is particularly favored in projects where developers want their work to be as accessible and reusable as possible, **including** in proprietary contexts. This flexibility and compatibility with other licenses have contributed to its popularity in the open-source community. 

- Permissive license allowing users to freely use, modify, and distribute the software.

- Requires including the original license and copyright notice in the distribution.

- Provides flexibility for commercial and proprietary use.

- Does not impose copyleft requirements on derivative works.

- Compatible with other licenses, including copyleft licenses.

#### BSD License:

The BSD License, originally developed at the University of California, Berkley, is another permissive license with terms similar to the BSD License, It allows redistribution and use in both source and binary forms, with or without modification. The key requirement for BSD Licenses is **attribution**: users **must** give proper credit to the original authors. That means, all code redistributed in source code format **must retain** the BSD License; all binaries redistributed **must reproduce** the license. As the BSD License places so few limitations on the use of the code, the license class is often used in academic and enterprise settings where flexibility is essential. Variants like the 2-Clause and 3-Clause BSD Licenses do provide some options on how much attribution/endorsement is required of the user.

- Permissive and highly compatible with other licenses.

- Allows reuse, modification, and redistribution.

- Requires proper attribution of original authors.

- Suitable for both academic and commercial use.

- Available in multiple variants (e.g., 2-Clause, 3-Clause, ...)

#### Apache License:

The Appache License provides a balance between openness and legal protection. Like the other licenses above it is quite permissive: It allows broad use, distribution, and modification of software, **but** it distinguishes itself through a strong emphasis on intellectual property rights. In particular, it includes a patent grant clause that protects users against patent claims from contributors. This legal clarity helps making it particularly attractive for commercial projects and larger-scale collaborations. Similar to the above licenses, the Appache License also requires the preservation of copyright and license notices and also includes a clear mechanism on handling contributions.

- Permissive license with legal safeguards.

- Includes explicit patent rights protection.

- Allows redistribution and modification, including for commercial use.

- Requires license and copyright notice in any redistributed versions.

- Compatible with many open-source as well as some proprietary licenses.

#### GNU General Public License (GPL):

The GNU GPL is a strong copyleft license designed to ensure that software remains free and open for all users. **Any** derivative work or modified version of the software **must** be licensed under the same terms, which ensures that freedom to use, modify, and share is preserved even throughout the software's evolution over time. The GNU GPL also requires that source code is publically available whenever the software - or derivatives thereof - are distributed. Thus, creating a culture of openness and collaboration in the userbase. The license is ideal for projects where the goal is to maintain a fully open ecosystem, but its strict requirements may limit compatibility to non-GPL software.

- Copyleft license that ensures derivative works are also licensed under the GPL.

- Requires distributing the source code of the software when distributing the software itself.

- Encourages sharing and collaboration within the open-source community.

- Version 2 (GPLv2) is widely used and compatible with GPLv3 but less compatible with other licenses.

- Version 3 (GPLv3) includes additional provisions for patent protection.

### Creative Commons (CC) Licenses 

Creative Commons (CC) licenses are a suite of standardized licenses designed to help creators share their work with the public under clear terms. Unlike the above mentioned licenses, CC licenses are used primarily for creative and academic content, including artwork, literature, media, and educational content. Compare this to the above mentioned licenses: Those are primarily used for software. The CC licenses are not recommended for software or hardware, yet they are widely used in academia for publication of data, documentation, and associated media. 
Various CC licenses exist, with different combinations of attribution, share-alike, and non-commercial clauses. They provides a framework for granting permissions and specifying usage restrictions. CC licenses offer flexibility in allowing creators to define the terms of use and distribution for their works.

CC licenses are built from combining four basic elements:
- Attribution (**BY**) - Credit must be given to the creator.
- Share Alike (**SA**) - Adaptations/Derivatives must be shared under the same license.
- Non-Commercial (**NC**) - Use is restricted to non-commercial purposes.
- No-Derivatives (**ND**) - No modifications or adaptations are allowed.

Each license type balances openness and control differently:

## CC0 (Public Domain Dedication)

The CC0 license specifically waives all rights and dedicates the work to the public domain. This allows **anyone** to freely use, modify, and distribute the work without asking for permission or having to give any credit. CC0 is the most permissive of the CC licenses and is often used for datasets and resources intended for unrestricted public access. The CC0 combines exactly 0 (hence the name) of the above-mentioned basic elements of the CC licenses.

- No rights reserved: completely free to uses, even commercially.
- No attribution required.
- Ideal for datasets, reference materials, and public domain works.
- Not recommended for software (consider using an open-source license instead)

## CC BY (Attribution)

The CC BY license allows others to distribute, adapt, modify, and build upon the work - even commercially - so long as appropriate credit to the original author is given. The Creative Commons Attribution license is one of the most open licenses and widely used in education and research.

- Allows modification and commercial use.
- Requires attribution to the original author.
- Supports wide dissemination and reuse.
- Compatible with open educational resource initiatives.

## CC BY-SA (Attribution-ShareAlike)

This license allows for adaptations and commercial use of the work, so long as attribution is given and any derivative works are licensed under identical terms. It thus mirrors the spirit of the GPL for creative content and promotes a copyleft style of reuse.

- Requires attribution and sharing under the same license.
- Allows commercial and non-commercial use.
- Encourages open sharing and collaborative development.
- Compatible with other "open-content" models.

## CC BY-ND (Attribution-NoDerivatives)

CC BY-ND is more restrictive. It permits redistribution for commercial and non-commercial use, as long as the work remains **unchanged** and the creator is properly credited. **No* derivatives are allowed of the work, thus making this license type useful when creators want their work to be shared widely, but without any modification.

- Allows redistribution with proper attribution.
- No modifications or adaptations are permitted.
- Suitable for finalized works like reports, graphics, or statements.
- Maintains the integrity of the original content.
- Not suitable for software projects.

## CC BY-NC (Attribution-NonCommercial)

This license lets other remix, adapt, and build upon the work. However it restricts the use of the work and its derivatives to non-commercial use only. It also requires proper attribution. The license is widely used in academic and non-profit contexts, where public sharing is encouraged but commercial exploitation should be restricted.

- Permits reuse and modification, but only for non-commercial purposes.
- Requires attribution to the original creator.
- Cannot be used in commercial projects.
- Popular in academic and educational settings.

## CC BY-NC-SA (Attribution-NonCommercial-ShareAlike)
The CC BY-NC-SA license combines the non-commercial and share-alike clauses. It allows users to remix, adapt, and build upon the work for non-commercial purposes, so long as the proper attribution is given and any derivatives are shared under identical terms.

- Non-commercial use only, with attribution.
- Derivative works must use the same license.
- Encourages non-commercial collaboration and content sharing.
- Common in academic and educational resources.

## CC BY-NC-ND (Attribution-NonCommercial-NoDerivatives)

This license is the most restrictive of the CC licenses. It allows the user to download and share the work with proper credit, but the users are not allowed to alter the work in any way, nor are they allowed to exploit the work commercially. It is best for creators who want their work circulated as-is, but do not wish for it to be changed or monetized.

- Redistribution allowed with attribution.
- No commercial use or derivative works are allowed.
- Suitable for sharing finished works as-is.
- Does not allow further use for adaptation. 

All CC licenses can be found [here](https://creativecommons.org/licenses/), including their full legal descriptions.

### Which License should you choose? 

Choosing the most suitable license for your project involves several important considerations.
First, it's essential to decide whether the work should be licensed at all, as some projects may be intended for private or restricted use only.
If the content includes source code, it's important to determine whether open-source licensing is appropriate, and if so whether you want to require that derivative works also share the source code for their adaptations.
Additionally, licensing may address patent rights. This may be crucial for any projects that includes state-of-the-art software or algorithms.
Compatibility with the licenses of any third-party software included in your project is another key factor: Incompatible licenses could create legal or logistical challenges moving forward.
Next, any institutional policies may impact your licensing options. Therefore, always check with your organization for guidelines or any requirements that it has in place for licensing works created while working there.
Finally, consulting with legal or copyright experts within your institution may help clear or clarify any complex issues that arise from your specific circumstances. This helps to ensure the chosen license both aligns with your goals for the work, and it remains legally sound in the environment surrounding your work.

You should consider the following questions:

- Do we want to license the work at all?
- Is the content we are licensing source code?
- Do we require people distributing derivative works to also distribute their code?
- Do we want to address patent rights?
- Is our license compatible with the licenses of the software we depend on?
- Do our institutions have any policies that may overrule our choices?
- Are there any copyright experts within our institution who can assist us?

You can get more help at: [Choosealicense.com](https://choosealicense.com/) 

**IMPORTANT:** **_Don’t write your own license. Legalese is a highly technical language, and words don’t mean what you think they do._**

