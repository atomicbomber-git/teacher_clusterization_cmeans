<template>
    <table class="table table-sm table-bordered">
        <thead class="thead thead-dark">
            <tr>
                <th> # </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nama')"> Nama </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('NIP')"> NIP </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('kelas')"> Kelas </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('kode_mk')"> Kode MK </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('mata_kuliah')"> Mata Kuliah </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_1')"> N1 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_2')"> N2 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_3')"> N3 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_4')"> N4 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_5')"> N5 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_6')"> N6 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_7')"> N7 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_8')"> N8 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_9')"> N9 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_10')"> N10 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_11')"> N11 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_12')"> N12 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_13')"> N13 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_14')"> N14 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_15')"> N15 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_16')"> N16 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('nilai_17')"> N17 </button> </th>
                <th> <button class="btn btn-link text-light" @click="sortBy('cluster')"> Cluster </button> </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(dosen, i) in orderedDosens" :key="dosen.pk">
                <td> {{ i + 1 }} </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nama')" type="text" max="100" v-model="dosen.fields.nama"> <button @click=deleteData(dosen) class="btn btn-sm btn-danger"> Hapus </button>  </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'NIP')" type="text" v-model="dosen.fields.NIP"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'kelas')" type="text" v-model="dosen.fields.kelas"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'kode_mk')" type="text" v-model="dosen.fields.kode_mk"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'mata_kuliah')" type="text" v-model="dosen.fields.mata_kuliah"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_1')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_1"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_2')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_2"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_3')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_3"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_4')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_4"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_5')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_5"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_6')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_6"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_7')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_7"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_8')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_8"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_9')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_9"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_10')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_10"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_11')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_11"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_12')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_12"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_13')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_13"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_14')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_14"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_15')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_15"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_16')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_16"> </td>
                <td> <input :class="{'border-danger': dosen.isUpdating}"  @change="updateData(dosen, 'nilai_17')" class="score" type="number" step="0.01" max="100" v-model="dosen.fields.nilai_17"> </td>
                <td> {{ dosen.fields.cluster }} </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import { debounce, keyBy, map, orderBy, sortBy } from "lodash";

export default {
  data() {
    return {
      dosens: orderBy(map(keyBy(window.dosens, "pk"), dosen => {
        return { ...dosen, isUpdating: false };
      }), 'fields.nama'),

      sort_by: 'nama',
      order: 'asc'
    };
  },

  computed: {
    orderedDosens() {
      return orderBy(this.dosens, `fields.${this.sort_by}`, [this.order])
    }
  },

  methods: {
    sortBy(field) {
      this.sort_by = field
      if (this.order == 'asc') {
        this.order = 'desc'
      } else {
        this.order = 'asc'
      }
    },

    updateData: debounce((dosen, field) => {
      dosen.isUpdating = true;
      axios
        .post("/update", {
          id: dosen.pk,
          field: field,
          value: dosen.fields[field]
        })
        .then(response => {
          dosen.isUpdating = false;
          console.log(response.data);
        })
        .catch(error => {
          dosen.isUpdating = false;
          alert("Update gagal");
        });
    }, 400),

    deleteData(dosen) {
        axios.post(`/delete/${dosen.pk}`)
          .then(response => {
            window.location.reload(true)
          })
          .catch(error => {
            alert(error)
          })
    }
  }
};
</script>

